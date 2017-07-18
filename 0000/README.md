## 第 0000 题

将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果 

![0000](http://oow6unnib.bkt.clouddn.com/show-me-the-code-0000.png)

## 题解

将原来的字库`arial.ttf` 换成 `Arial.ttf`，然后就可以成功了。


## 以下为之前的测试

没有成功，输出错误如下

```
▶ python img-addnum.py
206 245
Traceback (most recent call last):
	  File "img-addnum.py", line 23, in <module>
	      img_addnum('cat.jpg', '3')
	    File "img-addnum.py", line 17, in img_addnum
	      fnt = ImageFont.truetype('arial.ttf', int(h * 0.15))
	    File "/usr/local/lib/python2.7/site-packages/PIL/ImageFont.py", line 238, in truetype
	      return FreeTypeFont(font, size, index, encoding)
	    File "/usr/local/lib/python2.7/site-packages/PIL/ImageFont.py", line 127, in __init__
	      self.font = core.getfont(font, size, index, encoding)
	  IOError: cannot open resource
```

可能是字体库的问题，暂时搁浅
