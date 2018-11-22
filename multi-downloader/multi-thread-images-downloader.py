# -*- coding: utf-8 -*-
import os
from contextlib import closing
import threading
import requests
import time
import sys

# 输入图片url列表文件
img_lst = sys.argv[1]
# 输出文件夹
out_dir = './output'
# 线程数
thread_num = 32
# http请求超时设置
timeout = 5

# 下载并保存图片
def download(img_url, img_name):
    if os.path.isfile(os.path.join(out_dir, img_name)):
        return
    with closing(requests.get(img_url, stream=True, timeout=timeout)) as r:
        rc = r.status_code
        if 299 < rc or rc < 200:
            print('returnCode%s\t%s' % (rc, img_url))
            return
        try:
            with open(os.path.join(out_dir, img_name), 'wb') as f:
                for data in r.iter_content(1024):
                    f.write(data)
        except:
            print('savefail\t%s' % img_url)

# url和图片name生成器
def get_imgurl_generate():
    with open(img_lst, 'r') as f:
        index = 0
        for line in f:
            index += 1
            if index % 500 == 0:
                print('execute %s line at %s' % (index, time.time()))
            if not line:
                print(u'line %s is empty "\t"' % index)
                continue
            line = line.strip()
            imgs = ['url', 'name']
            try:
                imgs[0] = line
                imgs[1] = line.split('/')[-1]
                yield imgs
            except:
                print(u'line %s can not split by "\t"' % index)

def loop(imgs):
    print('thread %s is running...' % threading.current_thread().name)
    while True:
        try:
            with lock:
                # 加锁，保证只有一个线程可以获得下一个图片链接
                img_url, img_name = next(imgs)
        except StopIteration:
            break
        try:
            download(img_url, img_name)
        except:
            print('exceptfail\t%s' % img_url)
    print('thread %s is end...' % threading.current_thread().name)

if __name__=='__main__':
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    lock = threading.Lock()
    img_gen = get_imgurl_generate()

    for i in range(0, thread_num):
        t = threading.Thread(target=loop, name='LoopThread %s' % i, args=(img_gen,))
        t.start()
