'''import re

pattern = r'h.t\b'
text = 'hot hit het hrt hat hate hood heart'

res = re.findall(pattern,text)
print(res)
'''
'''
import re

pattern = r'^h'
text = 'hot hit het hrt hat hate hood heart'

res = re.findall(pattern,text)
print(res)
'''
'''
import re

pattern = r't$'
text = 'hot hit het hrt hat hate hood heart'

res = re.findall(pattern,text)
print(res)
'''
'''
import re

pattern = r'to*'
text = 'too to t tooooo'

res = re.findall(pattern,text)
print(res)
'''
'''
import re

pattern = r'to+'
text = 'too to t tooooo'

res = re.findall(pattern,text)
print(res)
'''
'''
import re

pattern = r'to?'
text = 'too to t tooooo'

res = re.findall(pattern,text)
print(res)
'''
'''
import re

pattern = r'to?\b'
text = 'too to t tooooo'

res = re.findall(pattern,text)
print(res)
'''
'''
import re

pattern = r'[a-z]{4}'
text = 'asdf sdf sd s'

res = re.findall(pattern,text)
print(res)
'''
'''
import re

pattern = r'[a-z]{3,4}'
text = 'asdf sdf sd s'

res = re.findall(pattern,text)
print(res)
'''
'''
import re

pattern = r'(python)'
text = 'pyth python pythin'

res = re.findall(pattern,text)
print(res)
'''
'''
import re

pattern = r'^[a-zA-Z]{2,15}( [a-zA-Z]{2,15})+$'
text =  input("Enter the text: ")
res = re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid Format")

'''
'''
import re
pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
text =  input("Enter the text: ")
res = re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid Format")
'''
'''
import re
pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
text =  input("Enter the text: ")
res = re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid Format")
'''
'''
import re
pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}'
text =  input("Enter the text: ")
res = re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid Format")
'''
'''
import re
pattern = r'^[a-zA-Z0-9]{5,15}$'
text =  input("Enter the text: ")
res = re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid Format")
'''
