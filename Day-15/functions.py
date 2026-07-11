'''
def function_name(arg):
   #stmts
   return

function_name(para)
'''
'''
def wish(name):
    print(f'Welcome to the python corse {name}!')

wish('subbu')
wish('praneeth')
wish('rishitha')
wish('saidurga')

'''
'''
def iseven(num):
    if num%2==0:
        return f"{num} - even number"
    else:
        return f"{num} - odd number"
print(iseven(12))
print(iseven(13))
'''
'''
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
num = int(input("enter the number:"))
print("factorail:",factorial(num))
'''
'''
def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num} - not prime number"
    return f"{num} - prime number"

num = int(input("enter the number:"))
print(isprime(num))'''
'''
def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("password:",pwd)

display(name='subbu',email='subbu@gmail.com',pwd='subbu@123')
'''
'''
def display(name,email,pwd=''):
    print("name:",name)
    print("email:",email)
    print("password:",pwd)

display(name='subbu',email='subbu@gmail.com')
'''
'''
#positional variable length
def display(*name):
    print("name:",name)
    
display('sathu','sathwii','sathwik','sathwika')
display('prava','paddhu','pravalika')
display('vasu','vasudha')
'''
'''

#kay word variable length
def display(**name):
    print("name:",name)
    
display(k1='sathu',k2='sathwii',k3='sathwik',k4='sathwika')
display(k1='prava',k2='paddhu',k3='pravalika')
display(k1='vasu',k2='vasudha')
'''
