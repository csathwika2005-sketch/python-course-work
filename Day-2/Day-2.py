Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import keyword
>>> 
===================================================== RESTART: C:/Users/karth/OneDrive/Desktop/python course work/Day-2/keywords.py ====================================================
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
Traceback (most recent call last):
  File "C:/Users/karth/OneDrive/Desktop/python course work/Day-2/keywords.py", line 3, in <module>
    print(len(keyword.kwlit))
AttributeError: module 'keyword' has no attribute 'kwlit'. Did you mean: 'kwlist'?
>>> 
===================================================== RESTART: C:/Users/karth/OneDrive/Desktop/python course work/Day-2/keywords.py ====================================================
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
>>> Myvar=10
>>> Myvar1=10
>>> Myvar@=10
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Myvar@=10
TypeError: unsupported operand type(s) for @=: 'int' and 'int'
>>> my_var=10
>>> my var=10
SyntaxError: invalid syntax
>>> myvar=10
>>> Myvar=10
>>> 1myvar=10
SyntaxError: invalid decimal literal
>>> _myvar=10
>>> it = 10
>>> if = 10
SyntaxError: invalid syntax
>>> var=10
>>> Var=20
>>> a=b=c=10
>>> 
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c=10,20,30
>>> a
10
b
20
c
30
