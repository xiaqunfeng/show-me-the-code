## 第 0011 题

敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

```
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
```

## fiter_word.py

**input():**

接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。

**输出:**

```
▶ python3 filter_word.py
please input your word:
sex
the result is:
Freedom
please input your word:
hello
the result is:
Human Rights
please input your word:
exit
```
