#date and time
'''from datetime import date,time,datetime,time
t = date.today()
print(t)
print("Year:", t.year)
print("Month:", t.month)
print("Day:",t.day)
print("Weekday from 0:", t.weekday())
print("Weekday from 1:", t.isoweekday())
'''
'''
from datetime import date,time,datetime,time
t = date(2026,2,6)
print(t)
'''
'''
from datetime import date,time,datetime,time
t = time(20,59,0)
print(t)
'''
'''
from datetime import date,time,datetime,time
t = datetime.now()
print(t)
'''
'''
from datetime import date,time,datetime,timedelta
n = datetime.now()

print(n.strftime('%d/%m/%y'))
print(n.strftime('%d/%m/%y %H:%M:%S'))
print(n.strftime('%d/%m/%y %I:%M:%S %p'))
print(n.strftime('%d/%b/%y %I:%M:%S %p'))
print(n.strftime('%d/%B/%y %I:%M:%S %p'))
print(n.strftime('%a, %d %B,%y %I:%M:%S %p'))
print(n.strftime('%A, %d %B,%y %I:%M:%S %p'))
'''
'''
from datetime import date,time,datetime,timedelta
n = datetime.now()
n15 = n + timedelta(minutes= 15)
n2 = n+ timedelta(hours= 2)
n7 = n-timedelta(days=1)
print(n15,n2,n7,sep='\n')
'''
#exption handling
'''
try:
    a= int(input("enter the age: "))
except ValueError:
    print("Enter the age in a digit[0-9] format")
else:
    print("Age:",a)
finally:
    print("thank you")
'''
'''
try:
    a=int(input("Enter the age:"))
    print(12/0)
    print(b)
    print(13+'14')
    d={1:1,2:2,3:3}
    print(d[5])
    l=[1,2,3]
    print(l[10])

except ValueError:
    print("Enter the age in digit [0-9] format")
except ZeroDivisionError:
    print("can't divide with zero")
except NameError:
    print("define the var")
except TypeError:
    print("add the same datatypes")
except KeyError:
    print("key is not present")
except IndexError:
    print("index is out of range")
else:
    print("Age:",age)
finally:
    print("thank you")
    '''
'''
try:
    a=int(input("Enter the age:"))
    print(12/0)
    print(b)
    print(13+'14')
    d={1:1,2:2,3:3}
    print(d[5])
    l=[1,2,3]
    print(l[10])
except(ValueError,ZeroDivisionError,NameError,TypeError,KeyError,IndexError) as e:
    print("Error occured:",e)
else:
    print("no error")
finally:
    print("thank you")
    '''
'''

try:
    a=int(input("Enter the age:"))
    print(12/0)
    print(b)
    print(13+'14')
    d={1:1,2:2,3:3}
    print(d[5])
    l=[1,2,3]
    print(l[10])
except Exception as e:
     print("Error occured:",e)
else:
    print("no error")
finally:
    print("thank you")
    
'''
try:
    amount = int(input("Enter the amount to withdraw: "))
    if amount < 0:
        raise Exception("Enter the amount greater then 0")
except Exception as e:
     print("Error occured:",e)
else:
    print("no error")
finally:
    print("thank you")
