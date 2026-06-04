 Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='     hello world         '
s
'     hello world         '
s.strip()
'hello world'
s.lstrip()
'hello world         '
s.rstrip()
'     hello world'
s='strings.py'
s
'strings.py'
s.startswith('str')
True
s.startswith('sdf')
False
s.endswith('py')
True
'sdfg'.is alpha
SyntaxError: invalid syntax
'sdfg'.isalpha()
True
'123'.isalnum()
True
'hello'.islower()
True
'Hello'.islower()
False
'HELLO'.isupper()
True
''.isspace()
False
' '.isspace()
True
'hello world'.istitle()
False
"hello world".istitle()
False
"Hello world".istitle()
False
"Hello World".istitle()
True
"variable1".isidentifier()
True

l=list()
type(l)
<class 'list'>
l=[1,2,3,4,5]
l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
result=l1+l2
result
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
printl*2
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    printl*2
NameError: name 'printl' is not defined. Did you mean: 'print'?
print(l*2)
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
l=[22,33,44,55,66]
print(s[1])
t
s[1]
't'
l[1]
33
l[:3]
[22, 33, 44]
l{::-]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
l[::-1]
[66, 55, 44, 33, 22]
l[-1:-4:-2]
[66, 44]
l
[22, 33, 44, 55, 66]
22 in l
True
22 not in l
False
False
False
l
[22, 33, 44, 55, 66]
id(l)
1846892017472
l[1]=20
l
[22, 20, 44, 55, 66]
id(l)
1846892017472
l.append(12)
l
[22, 20, 44, 55, 66, 12]
l.insert(4,44)
l
[22, 20, 44, 55, 44, 66, 12]
l.extend([1,2,3])
l
[22, 20, 44, 55, 44, 66, 12, 1, 2, 3]
l.pop()
3
l
[22, 20, 44, 55, 44, 66, 12, 1, 2]
l.pop(3)
55
l
[22, 20, 44, 44, 66, 12, 1, 2]
l.remove(44)
l
[22, 20, 44, 66, 12, 1, 2]
del l(2)
SyntaxError: cannot delete function call
del l(2)
SyntaxError: cannot delete function call
del l[2]
l
[22, 20, 66, 12, 1, 2]
l.clear()
l
[]
del l
l
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    l
NameError: name 'l' is not defined. Did you mean: 'l1'?
l=[12,23,34,45]
l
[12, 23, 34, 45]
sorted(l)
[12, 23, 34, 45]
l.sort()
min(l)
12
max(l)
45
l.reserve()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    l.reserve()
AttributeError: 'list' object has no attribute 'reserve'. Did you mean: 'reverse'?
l.reverse()
l
[45, 34, 23, 12]
sorted(l,reverse=True)
[45, 34, 23, 12]
>>> [45, 34, 23, 12]
[45, 34, 23, 12]
>>> l.index(12)
3
>>> l.count(45)
1
>>> #copy
>>> m=l
>>> m
[45, 34, 23, 12]
>>> m.append[2]
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    m.append[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> m=l.copy()
>>> m
[45, 34, 23, 12]
>>> m.append[22]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    m.append[22]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> lin(n)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    lin(n)
NameError: name 'lin' is not defined. Did you mean: 'bin'?
>>> len(n)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    len(n)
NameError: name 'n' is not defined
>>> m
[45, 34, 23, 12]
>>> m.append(22)
>>> m
[45, 34, 23, 12, 22]
>>> len(l)
4
>>> sum(l)
114
>>> any([123,345,0,12,1])
True
>>> all([123,345,0,12,1])
False
