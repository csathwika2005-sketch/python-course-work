'''s='python programing'
for ch in s:
    print (ch)
'''
'''l=['sugar','salt','oil']
for item in l:
    print(item)
'''
'''s={'laptop','mouse','keyboard','phone'}
for i in s:
    print (i)
    '''
'''s={'name':'subbu','batch':55,'course:'pfs','skill':['python','html']}
   for i in d:
   print(i,d[i])
'''
#range(start,stop+1,step)=>(0,n,1)
'''for i in range(1,11):
    print(i)
    

for i in range(2,51,2):
    print(i)

for i in range(5,101,5):
    print(i)

for i in range(20,0,-1):
    print(i)


for i in range(7):
    print(i)

'''
'''s='looping statements'
for i in range(len(s)):
    print(i,s[i])

l=[1,2,3,4]
for i in range(len(l)):
    print(i,l[i])

s='looping'
for i in enumerate(s):
    print(i[0],i[1])
    
l=[1,2,3,4]
for i in enumerate(l):
    print(i[0],i[1])
 
t=(1,2,3,4)
for i in enumerate(t):
    print(i[0],i[1])
    
k={3,4,5,6}
for i in enumerate(k):
    print(i[0],i[1])
'''

'''
for i in range(10):
    pass

for i in range(10):
    if 1==5:
        continue
    print(i)
 
for i in range(10):
    if i==5:
        break
    print(i)
s='looping statement'
for i in s:
    if i in 'aeioujnkdnkh':
        print(i)

      
l=[12,32,25,56,75,95,64,53,77]
for i in l:
    if i%2==0:
        print(i)'''
'''
d={'laptop':0,'phone':2,'chargers':3,'tab':1,'mouse':4}
for i in d:
    if d[i]:
        print(i)
        
t=(1,2,3,4,5,6)
for i in range(len(t)):
    print(i*t[i])
'''
names={'sathwika','paravalika','sathu','prava'}
for i in names:
    print(i.upper())
