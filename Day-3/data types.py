Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
type(a)
<class 'int'>
t=9.999
type(t)
<class 'float'>
c=12+8j
type(c)
<class 'complex'>
s='python
SyntaxError: unterminated string literal (detected at line 1)
s='python'
type(s)
<class 'str'>
s="ahchh"
type(s)
<class 'str'>
s='python'
id(s)
2035918945424
s='java'
id(s)
2035923958064
l=[1,2,3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
l=[1,2,3]
id(1)
140727582276024
l.append(50)
l.append(60)
l
[1, 2, 3, 50, 60]
id(l)
2035963157696
l=[1,2,3]
l
[1, 2, 3]
l=['post1.png',reel1.mp4]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    l=['post1.png',reel1.mp4]
NameError: name 'reel1' is not defined
>>> l=['post1.mp4','reel1.mp5']
>>> l
['post1.mp4', 'reel1.mp5']
>>> l=[]
>>> l=list()
>>> type(1)
<class 'int'>
>>> t=()
>>> t+(1,2,3,4)
(1, 2, 3, 4)
>>> t
()
>>> t=(1,2,34,53)
>>> t
(1, 2, 34, 53)
>>> type(t)
<class 'tuple'>
>>> s={1,2,34}
>>> type(s)
<class 'set'>
>>> s=set()
>>> s={234,456,678}
>>> s
{456, 234, 678}
>>> d={'name':'abc','age':100}
>>> d
{'name': 'abc', 'age': 100}
>>> type(d)
<class 'dict'>
>>> status=True
>>> status=FalSe
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    status=FalSe
NameError: name 'FalSe' is not defined. Did you mean: 'False'?
>>> status=True
>>> status=False
>>> type(status)
<class 'bool'>
>>> a= None
>>> type(a)
<class 'NoneType'>
