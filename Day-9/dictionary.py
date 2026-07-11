Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d[1}='int'
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
d[1]='int'
d[2]='float'
d[3]='string'
d[2.3]='float'
d
{1: 'int', 2: 'float', 3: 'string', 2.3: 'float'}
d[2+3j]='complex'
d
{1: 'int', 2: 'float', 3: 'string', 2.3: 'float', (2+3j): 'complex'}
d[4]=False
d
{1: 'int', 2: 'float', 3: 'string', 2.3: 'float', (2+3j): 'complex', 4: False}
d={}
d[1]=1
d[1]=3
d
{1: 3}
d[1]=1
d[2]=2.3
d[3]=2+3j
d[4]=
SyntaxError: invalid syntax
d[4]="sdf"
d[5]=[12]
d[5]=[1,2]
d[6]=(1,3)
d[7]={1,4}
d[8]={2:3}
d[9]=False
d
{1: 1, 2: 2.3, 3: (2+3j), 4: 'sdf', 5: [1, 2], 6: (1, 3), 7: {1, 4}, 8: {2: 3}, 9: False}
d[4]
'sdf'
d[9]
False
d={'sathwika':29,'pravalika':30,'karthik':31,'shashank':33}
d
{'sathwika': 29, 'pravalika': 30, 'karthik': 31, 'shashank': 33}
d['sathwika']
29
d['lohitha']
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    d['lohitha']
KeyError: 'lohitha'
d.get('lohitha')
d.get('lohitha','not found')
'not found'
d.get('sathwika','not found')
29
'sathwika'in d
True
'sathwika'not in d
False
d.keys()
dict_keys(['sathwika', 'pravalika', 'karthik', 'shashank'])
d.values()
dict_values([29, 30, 31, 33])
>>> d.items()
dict_items([('sathwika', 29), ('pravalika', 30), ('karthik', 31), ('shashank', 33)])
>>> sorted.d
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    sorted.d
AttributeError: 'builtin_function_or_method' object has no attribute 'd'
>>> sorted(d)
['karthik', 'pravalika', 'sathwika', 'shashank']
>>> max(d)
'shashank'
>>> min(d)
'karthik'
>>> d['saniya']=21
>>> d
{'sathwika': 29, 'pravalika': 30, 'karthik': 31, 'shashank': 33, 'saniya': 21}
>>> d.update[{'padhu':77,'sathu':22}]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    d.update[{'padhu':77,'sathu':22}]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> d.update({'padhu':77,'sathu':22})
>>> d
{'sathwika': 29, 'pravalika': 30, 'karthik': 31, 'shashank': 33, 'saniya': 21, 'padhu': 77, 'sathu': 22}
>>> d.popitem()
('sathu', 22)
>>> d.pop('saniya')
21
>>> del d['karthik']
>>> d
{'sathwika': 29, 'pravalika': 30, 'shashank': 33, 'padhu': 77}
>>> d.clear()
>>> d
{}
>>> d.setdefaullt('rishi':0)
SyntaxError: invalid syntax
>>> d.setdefaullt('rishi',0)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    d.setdefaullt('rishi',0)
AttributeError: 'dict' object has no attribute 'setdefaullt'. Did you mean: 'setdefault'?
>>> d.setdefault('rishi',0)
0
>>> d
{'rishi': 0}
