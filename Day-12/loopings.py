'''pin=1414
for i in range (5):
    e_pin = int(input("enter the pin:"))
    if e_pin == pin:
        print("unlock the phone")
        break
    else:
        print("incorrect pin")
else:
    print("try again, after 60 sec")
'''
'''
l=[2,3,4,6,7,9,75]
search = int(input("enter the element: "))

for i in range(len(l)):
    if l[i]==search:
        print(f'{search}is found at index-{i}')
        break
else:
    print(f'{search} is not found')
'''
'''
password = input("Enter the password:")
if len(Password)>=8:
    s=set()
    for i in password:
     if i.isupper():
         s.add('u')
     elif i.islower():
        s.add('l')
     else:
        s.add('s')
        
    if len(s)==4:
      print("strong password")
    else:
      print("weak password")
else:
    print("weak password")
'''
'''
status = True
assert status != None,"you need to update the status"
print(status)
'''
'''
name='abc'
batch=55
age=21
assert(name!=None and batch!=None and age!=None),"you need to update the data"
print(name,batch,age)
'''
'''
i=1
while i<11:
    print(i)
    i+=1
    '''
'''
i=2
while i<21:
    print(i)
    i+=2
'''
'''
i=5
while i<51:
    print(i)
    i+=5
'''
'''
i=10
while i>0:
    print(i)
    i-=1
'''
'''
l=[1,2,3,4,5,8,6,7]
i=0
while i<len(l):
    print(l[i])
    i+=1'''
'''
l="python programming"
i=0
while i<len(l):
    print(l[i])
    i+=1
    '''
'''
l=(1,2,3,4,5)
i=0
while i<len(l):
    print(l[i])
    i+=1
    '''
'''
l=[1,0,0,2,3,4,0,0,5,0,66,77,0,0,34]
while 0 in l:
    l.remove(0)
print(l)
'''
'''
moves=30
while moves>1:
    status=input(f"[W]in or [C]ontinue:").upper()
    if status == 'w':
        print("you won the game")
        break
    moves-=1
    print(f'{moves} moves are left')
else:
    print("Game over")
'''
