## 多线程下载

### 1、下载图片列表

过程：

- 将逐条图片信息加载进迭代器（使用yield）
- 每个线程依次取一个图片进行下载

使用方法：

```
▶ python3 multi-thread-images-downloader.py img_url_list.txt
```

### 2、下载某个文件

过程：

- 用request.head方法请求数据，得到http头信息，从中取出Content-length的值，即为数据长度。
- 确定几个线程，给每个线程确认要获取的数据区间，即range字段的值
- 每个线程取到相应内容，文件中seek到对应位置再写入

```
▶ python3 multi-thread-file-downloader.py http://xxxx/test_file.tar
文件 test_file.tar 大小为 62697984 bytes
####################################
Thread 0:	 start_pos[0] -> end_pos[7837248]
Thread 1:	 start_pos[7837248] -> end_pos[15674496]
Thread 2:	 start_pos[15674496] -> end_pos[23511744]
Thread 3:	 start_pos[23511744] -> end_pos[31348992]
Thread 4:	 start_pos[31348992] -> end_pos[39186240]
Thread 5:	 start_pos[39186240] -> end_pos[47023488]
Thread 6:	 start_pos[47023488] -> end_pos[54860736]
Thread 7:	 start_pos[54860736] -> end_pos[62697984]
####################################
[0 -> 7837248] 	download success
[23511744 -> 31348992] 	download success
[54860736 -> 62697984] 	download success
[31348992 -> 39186240] 	download success
[7837248 -> 15674496] 	download success
[15674496 -> 23511744] 	download success
[47023488 -> 54860736] 	download success
[39186240 -> 47023488] 	download success
####################################
文件 test_file.tar 下载完成!
耗时：49.486785 秒
```

## 知识点

需要import的模块

```
import os
from contextlib import closing
import threading
import requests
import time
import sys
```

简单的http协议头信息

