## 第 0016 题

纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

```
[
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]
```

将上述内容写到 numbers.xls 文件中，如下图所示：

![0016](http://oow6unnib.bkt.clouddn.com/show-me-the-code-0016.png)

## json

JSON 语法是 JavaScript 对象表示法语法的子集。

- 数据在名称/值对中
- 数据由逗号分隔
- 花括号保存对象
- 方括号保存数组

名称/值对包括字段名称（在双引号中），后面写一个冒号，然后是值：

```
"firstName" : "John"
```

JSON 对象在花括号中书写, 对象可以包含多个名称/值对：

```
{ "firstName":"John" , "lastName":"Doe" }
```

JSON 数组在方括号中书写, 数组可包含多个对象：

```
{
"employees": [
    { "firstName":"John" , "lastName":"Doe" },
    { "firstName":"Anna" , "lastName":"Smith" },
    { "firstName":"Peter" , "lastName":"Jones" }
  ]
}
```

## 题解

0014和0015都是对象，这里就是简单的数组，所以直接遍历然后写入excel中即可

