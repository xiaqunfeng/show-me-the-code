## 第 0023 题

使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。

[阅读资料：Python 有哪些 Web 框架](http://v2ex.com/t/151643#reply53)

![0023](http://oow6unnib.bkt.clouddn.com/show-me-the-code-0023.jpeg)

## 题解

### 运行命令：

```
▶ python3 flaskr.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 145-998-354
127.0.0.1 - - [22/Jul/2017 22:34:00] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [22/Jul/2017 22:34:36] "POST /add HTTP/1.1" 302 -
127.0.0.1 - - [22/Jul/2017 22:34:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [22/Jul/2017 22:35:10] "POST /add HTTP/1.1" 302 -
127.0.0.1 - - [22/Jul/2017 22:35:10] "GET / HTTP/1.1" 200 -
^C%
```

### 结果

在浏览器中输入：`http://localhost:5000` ，留言实测如下：

![flaskr](http://oow6unnib.bkt.clouddn.com/flaskr.jpg)

## 知识点学习

这里选择flask作为web框架

安装 virtualenv

```
▶ pip3 install virtualenv
Collecting virtualenv
  Downloading virtualenv-15.1.0-py2.py3-none-any.whl (1.8MB)
    100% |████████████████████████████████| 1.8MB 106kB/s
Installing collected packages: virtualenv
Successfully installed virtualenv-15.1.0
```

安装flask

```
▶ pip3 install flask
Collecting flask
  Downloading Flask-0.12.2-py2.py3-none-any.whl (83kB)
    100% |████████████████████████████████| 92kB 385kB/s
Collecting Werkzeug>=0.7 (from flask)
  Downloading Werkzeug-0.12.2-py2.py3-none-any.whl (312kB)
    100% |████████████████████████████████| 317kB 2.9MB/s
Collecting click>=2.0 (from flask)
  Downloading click-6.7-py2.py3-none-any.whl (71kB)
    100% |████████████████████████████████| 71kB 6.4MB/s
Collecting itsdangerous>=0.21 (from flask)
  Downloading itsdangerous-0.24.tar.gz (46kB)
    100% |████████████████████████████████| 51kB 4.0MB/s
Collecting Jinja2>=2.4 (from flask)
  Downloading Jinja2-2.9.6-py2.py3-none-any.whl (340kB)
    100% |████████████████████████████████| 348kB 5.1MB/s
Collecting MarkupSafe>=0.23 (from Jinja2>=2.4->flask)
  Downloading MarkupSafe-1.0.tar.gz
Building wheels for collected packages: itsdangerous, MarkupSafe
  Running setup.py bdist_wheel for itsdangerous ... done
  Stored in directory: /Users/xiaqunfeng/Library/Caches/pip/wheels/fc/a8/66/24d655233c757e178d45dea2de22a04c6d92766abfb741129a
  Running setup.py bdist_wheel for MarkupSafe ... done
  Stored in directory: /Users/xiaqunfeng/Library/Caches/pip/wheels/88/a7/30/e39a54a87bcbe25308fa3ca64e8ddc75d9b3e5afa21ee32d57
Successfully built itsdangerous MarkupSafe
Installing collected packages: Werkzeug, click, itsdangerous, MarkupSafe, Jinja2, flask
Successfully installed Jinja2-2.9.6 MarkupSafe-1.0 Werkzeug-0.12.2 click-6.7 flask-0.12.2 itsdangerous-0.24
```

参考资料：照着[flask中文文档](http://docs.jinkan.org/docs/flask/tutorial/introduction.html)一步一步搭即可