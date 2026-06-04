Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=(12,23,34)
t
(12, 23, 34)
h=(45,54,11)
t+h
(12, 23, 34, 45, 54, 11)
t*4
(12, 23, 34, 12, 23, 34, 12, 23, 34, 12, 23, 34)
t=
SyntaxError: invalid syntax
t=(10,20,32,40,50)
t[:1]
(10,)
t=(10 ,20 ,32 ,40 ,50)
t[:1]
(10,)
t
(10, 20, 32, 40, 50)
t[2:4]
(32, 40)
t[::-1]
(50, 40, 32, 20, 10)
t[-2:-5]
()
t[-2:]
(40, 50)
t[5]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t[5]
IndexError: tuple index out of range
t
(10, 20, 32, 40, 50)
20 in t
True
20 not in t
False
len(t)
5
sort(t)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    sort(t)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
sorted(t)
[10, 20, 32, 40, 50]
min(t)
10
max(t)
50
sum(t)
152
t.count(10)
1
t.index(10)
0
a=(1,2,3)
a
(1, 2, 3)
x,y,z=a
x
1

y
2
z
3
t=(1,2,3,[4,5,9]6,7)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
t=(1,2,3,[4,5,9],6,7)
t
(1, 2, 3, [4, 5, 9], 6, 7)
t[2]
3
t[3]
[4, 5, 9]
t[2]=4
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
t[3].append(10)
t
(1, 2, 3, [4, 5, 9, 10], 6, 7)
s={1,2,3,4}
s=set()
s={1,1,1,1}
s
{1}
s={243,543,11,678,477,47}
s
{243, 678, 11, 543, 477, 47}
s=set()
s
set()
s.add(1)
s
{1}
s.add(12.34)
s
{1, 12.34}
s.add("dfg")
s
{'dfg', 1, 12.34}
s.add("True")
s
{'dfg', 1, 12.34, 'True'}
s.add("False")
s
{1, 'dfg', 12.34, 'True', 'False'}
1 in s
True
1 not in s
False
false not in s
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    false not in s
NameError: name 'false' is not defined. Did you mean: 'False'?
False not in s
True
a={1,3,5,6,1,2,6}
b={9,8}
a | b
{1, 2, 3, 5, 6, 8, 9}
a.union(b)
{1, 2, 3, 5, 6, 8, 9}
a intersection(b)
SyntaxError: invalid syntax
a.intersection(b)
set()
a&b
set()
a^b
{1, 2, 3, 5, 6, 8, 9}
b={9,8,1}
a&b
{1}
a.intersection(b)
{1}
a-b
{2, 3, 5, 6}
a
{1, 2, 3, 5, 6}
a
{1, 2, 3, 5, 6}
a <= 1
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a <= 1
TypeError: '<=' not supported between instances of 'set' and 'int'
a <= {1}
False
a >= {1}
True
a.isdisjoint({456,789})
True
a
{1, 2, 3, 5, 6}
b={1,5,8,9}
b
{8, 1, 5, 9}
a.isdisjoint(b)
False
a.add(17)
a
{1, 2, 3, 17, 5, 6}
a.update({11,23})
a
{1, 2, 3, 17, 5, 6, 23, 11}
a.pop()
1
a.remove(6)
a
{2, 3, 17, 5, 23, 11}
a.discard(6)
a
{2, 3, 17, 5, 23, 11}
a.clear()
a
set()
a
set()
a={12,21,23,42}
b={87,445,32}
a.symmetric_update(b)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a.symmetric_update(b)
AttributeError: 'set' object has no attribute 'symmetric_update'
>>> a.intersection_update(b)
>>> a
set()
>>> a={12,21,23,42}
>>> b={87,445,32}
>>> a
{42, 12, 21, 23}
>>> b
{32, 445, 87}
>>> a.intersection_update(b)
>>> a
set()
>>> b
{32, 445, 87}
>>> a.symmetric_update(b)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a.symmetric_update(b)
AttributeError: 'set' object has no attribute 'symmetric_update'
>>> a.difference_update(b)
>>> a
set()
>>> b
{32, 445, 87}
>>> a={12,21,23,42}b={87,445,32}
SyntaxError: invalid syntax
>>> a={12,21,23,42}
>>> b={87,445,32,42}
>>> a.difference_update(b)
>>> a
{12, 21, 23}
>>> b
{32, 42, 445, 87}
>>> len(b)
4
>>> min(b)
32
>>> max(b)
445
>>> sorted(b)
[32, 42, 87, 445]
>>> sum(b)
606
