Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> a
10
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> str(a)
'10'
>>> bool(a)
True
>>> c=2+3j
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> type(c)
<class 'complex'>
>>> set(c)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
>>> str(c)
'(2+3j)'
>>> bool(c)
True
>>> a=10.0
>>> int(a)
10
>>> complex(a)
(10+0j)
>>> str(a)
'10.0'
>>> bool(a)
True
>>> s='python'
>>> a='23456'
>>> b='3567.765'
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
int(a)
23456
float(s)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'python'
float(a)
23456.0
float(b)
3567.765
a=[1,2,3,4]
str(a)
'[1, 2, 3, 4]'
tuple(a)
(1, 2, 3, 4)
set(a)
{1, 2, 3, 4}
bool(a)
True
t=(1,2,3,4)
str(t)
'(1, 2, 3, 4)'
list(t)
[1, 2, 3, 4]
set(t)
{1, 2, 3, 4}
bool(t)
True
s={1,2,3,4,5}
list(s)
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
tuple(s)
(1, 2, 3, 4, 5)
bool(s)
True
str(s)
'{1, 2, 3, 4, 5}'
a={2:3,3:4,4:5}
str(a)
'{2: 3, 3: 4, 4: 5}'
list(a)
[2, 3, 4]
set(a)
{2, 3, 4}
tuple(a)
(2, 3, 4)
set(a)
{2, 3, 4}
bool(a)
True
