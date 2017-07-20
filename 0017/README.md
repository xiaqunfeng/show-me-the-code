## 第 0017 题

将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如下所示：

```
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
{
	"1" : ["张三", 150, 120, 100],
	"2" : ["李四", 90, 99, 95],
	"3" : ["王五", 60, 66, 68]
}
</students>
</root>
```

### 输出结果

```
▶ python3 excel2xml.py

▶ cat student.xml
<?xml version="1.0" encoding="UTF-8"?>
<root><students>
{
    "1": "['张三', 150.0, 120.0, 100.0]",
    "2": "['李四', 90.0, 99.0, 95.0]",
    "3": "['王五', 60.0, 66.0, 68.0]"
}
<!--
	学生信息表
	"d" :[名字, 数学, 语文, 英语]
--></students></root>
```

## 知识点

在[0014题](https://github.com/xiaqunfeng/show-me-the-code/tree/master/0014)的 README.md 中已经说过, 将数据写入excel中使用库 `xlwt` ，从excel中读取数据需要用到的库是 `xlrd`。

## xlrd

安装:

```
▶ pip3 install xlrd
Collecting xlrd
  Downloading xlrd-1.0.0-py3-none-any.whl (143kB)
    100% |████████████████████████████████| 153kB 1.6MB/s
Installing collected packages: xlrd
Successfully installed xlrd-1.0.0
```

打开文件：

```
excel = xlrd.open_workbook("test.xls")  
```

获取表格：

```
table = excel.sheets()[0]            #通过索引获取
table = excel.sheet_by_index(0)      #通过索引获取
table = excel.sheet_by_name('set')   #通过表名获取
```

获取表格的数据：

```
nrows = table.nrows                 #行数
ncols = table.ncols                 #列数
data = table.cell(nrow, ncol).value #得到表格数据
#获取每行每列的数据
for i in range(0, nrows):
    for j in range(0, ncols):
        data = table.cell(i, j).value
```

## xml

安装：

```
▶ pip3 install lxml
Collecting lxml
  Downloading lxml-3.8.0-cp36-cp36m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (7.8MB)
    100% |████████████████████████████████| 7.9MB 152kB/s
Installing collected packages: lxml
Successfully installed lxml-3.8.0
```

关于 `lxml.etree` 的使用：http://lxml.de/tutorial.html

## codecs

具体接口可以查看官方文档：[codecs — Codec registry and base classes](https://docs.python.org/3/library/codecs.html)

```
codecs.open(filename, mode='r', encoding=None, errors='strict', buffering=1)
```

功能：以给定的模式打开编码文件，并返回StreamReaderWriter的实例，提供透明的编码/解码。 默认文件模式为'r'（以读取模式打开文件）。

```
codecs.encode(obj, encoding='utf-8', errors='strict')
codecs.decode(obj, encoding='utf-8', errors='strict')
```

功能：使用 codec 编码/解码 obj

### 编解码

字符串在Python内部的表示是Unicode编码，因此，在做编码转换时，通常需要以Unicode作为中间编码，即先将其他编码的字符串解码（decode）成Unicode，再从Unicode编码（encode）成另一种编码。在python3中，取消了unicode类型，代替它的是使用unicode字符的字符串类型(str):

```
      decode              encode
bytes ------> str(unicode)------>bytes
```

举例：

```
u = '中文' 					#指定字符串类型对象u 
str = u.encode('gb2312') 	#以gb2312编码对u进行编码，获得bytes类型对象str 
u1 = str.decode('gb2312')	#以gb2312编码对字符串str进行解码，获得字符串类型对象u1 
u2 = str.decode('utf-8')	#如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的字符串内容
```

所以，文件保存时使用的编码格式，决定了我们从文件读取的内容的编码格式。

例如，我们从记事本新建一个文本文件test.txt,，编辑内容，保存的时候注意，编码格式是可以选择的，例如我们可以选择gb2312，那么使用python读取文件内容，方式如下：

```
f = open('test.txt','r')
s = f.read() #读取文件内容,如果是不识别的encoding格式（识别的encoding类型跟使用的系统有关），这里将读取失败

'''假设文件保存时以gb2312编码保存'''
u = s.decode('gb2312') #以文件保存格式对内容进行解码，获得unicode字符串

'''下面我们就可以对内容进行各种编码的转换了'''
str = u.encode('utf-8')#转换为utf-8编码的字符串str
str1 = u.encode('gbk')#转换为gbk编码的字符串str1
str1 = u.encode('utf-16')#转换为utf-16编码的字符串str1
```

### 使用codecs进行文件的读取

python给我们提供了一个包codecs进行文件的读取，这个包中的open()函数可以指定编码的类型：

```
import codecs 
f = codecs.open('text.text','r+',encoding='utf-8')	#必须事先知道文件的编码格式，这里文件编码是使用的utf-8 
content = f.read()									#如果open时使用的encoding和文件本身的encoding不一致的话，那么这里将将会产生错误 
f.write('你想要写入的信息') 
f.close()
```

以上关于codecs参考的[这里](http://www.cnblogs.com/ccorz/p/6089322.html)