# coding: utf-8
import requests
import threading
import os
import sys
import time
import datetime

lock = threading.Lock()

class downloader:
    # 构造函数
    def __init__(self):
        # 设置url
        self.url=sys.argv[1]
        # 设置线程数
        self.num=8
        # 文件名从url最后取
        self.name=self.url.split('/')[-1]
        # 用head方式去访问资源
        r = requests.head(self.url)
        # 取出资源的字节数
        self.size = int(r.headers['Content-Length'])
        print('文件 %s 大小为 %s bytes' % (self.name, self.size))
        print('####################################')

    def get_range(self):
        ranges=[]
        # 比如size是50,线程数是4个。offset就是12
        offset = int(self.size/self.num)
        for i in  range(self.num):
            if i==self.num-1:
                # 最后一个线程，不指定结束位置，取到最后
                #ranges.append((i*offset,''))
                ranges.append((i*offset,self.size))
            else:
                # 没个线程取得区间
                ranges.append((i*offset,(i+1)*offset))
        # range大概是[(0,12),(12,24),(25,36),(36,'')]
        return ranges
            
    def download(self,start,end):
        headers={'Range':'Bytes=%s-%s' % (start,end),'Accept-Encoding':'*'}
        # 获取数据段
        res = requests.get(self.url,headers=headers, stream=True)
        # 加锁，seek到指定位置写文件
        lock.acquire()
        self.fd.seek(start)
        self.fd.write(res.content)
        lock.release()
        print('[%s -> %s] \tdownload success' % (start,end))

    def run(self):
        # 打开文件，文件对象存在self里
        self.fd =  open(self.name,'wb')
        self.fd.truncate(self.size)

        thread_list = []
        n = 0
        start_time = time.time()
        #start_time = datetime.datetime.now().replace(microsecond=0)
        for ran in self.get_range():
            start,end = ran
            print('Thread %d:\t start_pos[%s] -> end_pos[%s]'%(n,start,end))
            n+=1
            # 开线程
            thread = threading.Thread(target=self.download,args=(start,end))
            thread.start()
            thread_list.append(thread)
        print('####################################')
        for i in thread_list:
            # 设置等待
            i.join()
        end_time = time.time()
        #end_time = datetime.datetime.now().replace(microsecond=0)
        print('####################################')
        print('文件 %s 下载完成!\n耗时：%f 秒' % (self.name, end_time-start_time))
        self.fd.close()

if __name__=='__main__':
    # 新建实例
    down = downloader()
    # 执行run方法
    down.run()
