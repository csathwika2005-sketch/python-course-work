Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=20
b=30
a+b
50
a-b
-10
a*b
600
a/b
0.6666666666666666
a//b
0
a%b
20
a**b
1073741824000000000000000000000000000000
a**2
400
a<b
True
a>b
False
a<=b
True
a>=b
False
a==b
False
a!=b
True
a=b
y=5
y
5
y=y+5
y
10
y=y+10
y
20
y+=10
y
30
y-=10
y
20
y
20
y*=4
y
80
y//10
8
y%=2
y
0
y+=10
y
10
y/=2
y
5.0
a=10
b=20
a
10
b
20
a%20==0 and b%20==0 and a<b
False
a%20==0 or b%20==0 or a<b
True
a%20==0 or b%20==0 or a>b
True
not a>b
True
#str,list,tuple,set,dict
a = 'python programming'
a
'python programming'
y is in a
SyntaxError: invalid syntax
y in a
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    y in a
TypeError: 'in <string>' requires string as left operand, not float
a = 'python programming'
a
'python programming'
y in a
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    y in a
TypeError: 'in <string>' requires string as left operand, not float
'y' in a
True
'y' not in a
False
'z' in a
False
l=['java','python','html']
python in l
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    python in l
NameError: name 'python' is not defined
'python' in l
True
'mysql' in l
False
'mysql' not in l
True
t={1,2,3,4}
5 in t
False
2 in t
True
2 not in t
False
s=(1,3,4,9)
6 in s
False
3 not in s
False
3 in s
True
d={'apple':18,'mango':20}
apple in d
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    apple in d
NameError: name 'apple' is not defined. Did you mean: 'tuple'?
'apple' in d
True
'banana' in d
False
'banana' not in d
True
l=[1,2,3,4]
m=[1,2,3,4]
l==m
True
n=m
n
[1, 2, 3, 4]
n==m
True
l is m
False
n is m
True
id(n)
3266838748224
id(m)
3266838748224
id(l)
3266838814080
l is not m
True
n is not m
False
8 & 14
8
8 & 7
0
8 | 7
15
10^11
1
~12
-13
~-13
12
>>> 8>>9
0
>>> 8>>4
0
>>> 9>>2
2
>>> 2<<8
512
>>> 4<<2
16
>>> 16
16
>>> a=12
>>> b=12.34
>>> c=python
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    c=python
NameError: name 'python' is not defined
>>> a=12
>>> b=12.34
>>> c="python
SyntaxError: unterminated string literal (detected at line 1)
>>> c="python"
>>> print(a,b,c)
12 12.34 python
>>> print("a="a,"b="b,"c="c)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("a=",a,"b=",b,"c=",c)
a= 12 b= 12.34 c= python
>>> print("a=",a,"b=",b,"c=",c,sep="",end='@@@')
a=12b=12.34c=python@@@
>>> print(f'a={a} b={b} c={c}')
a=12 b=12.34 c=python
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
a=12 b=12.34 c=python
>>> print('a={} b=
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print('a={} b={} c={}'.format(a,b,c))
...       
a=12 b=12.34 c=python
>>> print('a={2} b={0} c={1}'.format(a,b,c))
...       
a=python b=12 c=12.34
