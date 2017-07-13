## 第 0007 题

有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

## count_line.py

1、分别列出每个文件里对应的行数

2、列出所有文件总的对应行数

3、当文件夹里含有其他文件夹时，递归查找并统计

4、可以准确统计C、C++、python三种语言的代码

**代码文件夹`mycode`详情**

```
▶ tree mycode
mycode
├── code2
│   └── Messenger.cc
├── mypy.py
└── test.c

1 directory, 3 files
```

**测试结果**

```
▶ python3 count_code.py
Messenger.cc    : all_lines(31)	 code_lines(21)	 space_lines(3)	 comments_lines(7)
mypy.py         : all_lines(35)	 code_lines(27)	 space_lines(5)	 comments_lines(3)
test.c          : all_lines(31)	 code_lines(21)	 space_lines(3)	 comments_lines(7)

**** TOTAL COUNT ****
all_lines = 97
code_lines = 69
space_lines = 11
comments_lines = 17
```

>当前目录下的 test.py 和 test.c 是我用来测试匹配注释的临时代码，保留

**问题**

```
UnboundLocalError: local variable '' referenced before assignment
```

函数内部是可以访问全局变量的，问题在于函数内部修改了变量，导致python认为它是一个局部变量。

所以，如果在函数内部访问并修改全局变量，应该使用关键字 `global` 来修饰变量

