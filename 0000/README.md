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
