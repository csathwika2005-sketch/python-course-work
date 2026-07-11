'''def display():
    n=10
    print("inside:",n)
    
display()
print("outside:",n)'''
'''
n=10

def display():
    print("Inside:",n)
display()
print("outside:",n)'''
'''
def display():
    global n
    n=10
    print("Inside:",n)
display()
print("outside:",n)
'''
'''
def display():
    global n
    n+=10
    print("Inside:",n)
n=10
display()
print("outside:",n)
'''
'''
def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner function:",n)
    inner()
    print("Outer function:",n)
outer()
'''
'''
s='python'
print(len(s))

len=5
print(len(s))
'''
#int float complex str list tuple set dict
# int float complex str tuple bool
#list set dict
'''
def update(n):
    n= False
    print("Inside:",n)
n= True
update(n)
print("outside:",n)
'''
'''
def update(n):
    n+= (12,3)
    print("Inside:",n)
n= (2,3,4)
update(n)
print("outside:",n)
'''
'''
def update(n):
    n.append(10)
    print("Inside:",n)
n= [1,2,3]
update(n)
print("outside:",n)
'''
'''
def update(n):
    n+= 2
    print("Inside:",n)
n= 3+4j
update(n)
print("outside:",n)
'''
'''
def update(n):
    n+= "lang"
    print("Inside:",n)
n= "python"
update(n)
print("outside:",n)
'''
'''
def update(n):
    n[4]= 4
    print("Inside:",n)
n= {2:3,3:4}
update(n)
print("outside:",n)
'''
'''
def fun():
    is basecondi:
        return
    func()
'''
'''
def func(num):
    if num == 0:
        return
    print(num,end='')
    func(num-1)
func(5)
'''
'''
def func(num):
    if num == 0:
        return
    
    func(num-1)
    print(num,end='')
func(5)
'''
'''
def sumofdigits(n):
    if n==0:
        return 0
    return n+sumofdigits(n-1)
print(sumofdigits(5))
'''
'''
def sumofdigits(n):
    if n==0:
        return 1
    return n*sumofdigits(n-1)
print(sumofdigits(5))
'''
'''
def power(base,pow):
    if pow==0:
        return 1
    return base * power(base,pow-1)

print(power(2,4))
'''
'''
def reverseofstr(s,ind):
    if ind == 0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)
l="python programming"
print(reverseofstr(1,len(l)-1))
'''
