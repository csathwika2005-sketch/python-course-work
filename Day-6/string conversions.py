Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s1="hello"
s2="world"
total=s1+s2
total
'helloworld'
a="20"
print(a*2)
2020
s="sathwika"
print(s[1])
a
print(s[0],s[6])
s k
print(s[:6])
sathwi
len(s)
8
max(s)
'w'
min(s)
'a'
sorted(s)
['a', 'a', 'h', 'i', 'k', 's', 't', 'w']
chr(98)
'b'
ord(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    ord(a)
TypeError: ord() expected a character, but string of length 2 found
ord('a')
97
s.upper()
'SATHWIKA'
s.lower()
'sathwika'
s.capitalize()
'Sathwika'
s.swapcase()
'SATHWIKA'
s="STRAẞEMÁLAGAÅngströmCaf"
s.casefold(s)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.casefold(s)
TypeError: str.casefold() takes no arguments (1 given)
>>> s.casefold()
'strassemálagaångströmcaf'
>>> s="python programing"
>>> s.center(34,"*")
'********python programing*********'
>>> ljust(5"_")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> ljust(5,"_")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    ljust(5,"_")
NameError: name 'ljust' is not defined. Did you mean: 'list'?
>>> s.ljust(5,"_")
'python programing'
>>> s.rjust(5,"_")
'python programing'
>>> s.rjust(44,"_")
'___________________________python programing'
>>> s.ljust(44,"_")
'python programing___________________________'
>>> zfill(33)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    zfill(33)
NameError: name 'zfill' is not defined
>>> s.zfill(33)
'0000000000000000python programing'
>>> s="python programing"
>>> s.find(y)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s.find(y)
NameError: name 'y' is not defined
>>> s.find("y")
1
>>> s.rfind("p")
7
>>> index(s)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    index(s)
NameError: name 'index' is not defined
>>> s.index()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s.index()
TypeError: index() takes at least 1 argument (0 given)
s.index("o")
4
s.rindex("p")
7
s.count()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s.count()
TypeError: count() takes at least 1 argument (0 given)
s.count("a")
1
s="python"
s.replace("python","java")
'java'
s.maketrans("python","123")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s.maketrans("python","123")
ValueError: the first two maketrans arguments must have equal length
s.maketrans("python","123456")
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.maketrans("python","123456"))
'123456'
s=("python","java","css")
s.split(,)
SyntaxError: invalid syntax
s.split(",")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s.split(",")
AttributeError: 'tuple' object has no attribute 'split'
s=("python,java,css")
s.split(",")
['python', 'java', 'css']
s.split(',',2)
['python', 'java', 'css']
s.rsplit(',',3)
['python', 'java', 'css']
g="python
SyntaxError: unterminated string literal (detected at line 1)
g='pythin
SyntaxError: unterminated string literal (detected at line 1)
g= 'python
SyntaxError: unterminated string literal (detected at line 1)
g= 'python'
g='''hgsvb;
gbhhn;
hsbjk'''
g.splitline()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    g.splitline()
AttributeError: 'str' object has no attribute 'splitline'. Did you mean: 'splitlines'?
g.splitlines()
['hgsvb;', 'gbhhn;', 'hsbjk']
g.join()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    g.join()
TypeError: str.join() takes exactly one argument (0 given)
join()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    join()
NameError: name 'join' is not defined
t="hello"
t.encode()
b'hello'
b'hello'.decode()
'hello'
