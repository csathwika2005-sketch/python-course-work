'''
syntax:
var = lambds agr: exp
add = lambda a,b: a+b
print(add(12,13))
print(add(19,33))
'''
'''
wish = lambda name: f'welcome the python course {name}'
print(wish('sathu'))
print(wish('sathwi'))
'''
'''
gst = lambda price: price + price*0.18
print(gst(1000))
print(gst(100))
print(gst(800))
'''
'''
greatest = lamb
da a,b: a if a>b else b
print(greatest(18,10))
print(greatest(187,1000))
print(greatest(1899,2000))
'''
'''
iseven = lambda a: f"{a}-Even number" if a%2==0 else f"{a}-odd number"
print(iseven(4))
print(iseven(8))
print(iseven(9))
'''
'''
bill = lambda charge: charge if charge>99 else charge + 30
print(bill(14))
print(bill(900))
print(bill(143))
'''
'''
login = True
instock = True
status = lambda login,instock :("you can buy product" if instock else "product is out of stock") if login else "Login to buy a product"
print(status(login,instock))
'''
'''
l=[1,2,3,4,5,6,7]
res = list(map(lambda i:i**3,l))
print(res)

names = ['subbu','sath','sathwii']
t = list(map(lambda i:i.title(),names))
print(res)
'''
'''
l=[1,2,3,4,5,6,7,8,9,10,11]
res = list(filter(lambda i:i%2==0,l))
print(res)
l=[1,2,3,4,5,6,7]
res = list(filter(lambda i:i>5,l))
print(res)
l=[1,2,3,4,5,6,7]
res = list(filter(lambda i:i%3==0,l))
print(res)
'''
'''
from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10]
s = reduce(lambda sum,i: sum+i,l)
p = reduce(lambda pro,i: pro*i,l)
print(s,p)
'''
'''
from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10]
s = reduce(lambda sum,i: sum+i,l)
p = reduce(lambda pro,i: pro*i,l)
m = reduce(lambda max,i: max if max>i else i,l)
n = reduce(lambda min,i: min if min<i else i,l)
print(s,p)
'''
d = {'sathwika':20,'sathu':40,'prava':25,'vasu':23}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))

print(dict(sorted(d.items(),reverse= True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse= True)))
