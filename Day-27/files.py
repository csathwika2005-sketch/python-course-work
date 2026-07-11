'''file = open('sample.txt','r')

print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())

file.close()
'''
'''
try:
    file = open('sample.txt','r')
except FileNotFoundError:
    print("File os not there")
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()
'''
'''
with open('sample.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
'''
'''
with open('samples.txt','w') as file:
    file.write('vasu\npravalika\nsathwii')
'''
'''
with open('demo.txt','w+') as file:
    file.write('vasu\npravalika\nsathwii')
    file.seek(0)
    print(file.read())
'''
import os
import shutil
print(os.listdir('.')
      
#os.mkdir('sampllllle')
#os.makedirs('sampllllle/demo')
path = os.path.join('sampllllle/demo','demo.txt')
with open(path,'w+')as file:
    file.write("hello world")
    file.seek(0)
    print(file.read())
    
        
#os.rmdir('sampllllle')

