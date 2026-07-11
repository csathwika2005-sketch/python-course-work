'''import re

pattern = '[abc]'
text = 'codegnan'

res = re.match(pattern,text)

print(res.group() if res else "No Match Found")
'''
'''
import re

pattern = '[a - z]'
text = 'codegnan'

res = re.search(pattern,text)

print(res.group() if res else "No Match Found")
'''
'''
import re

pattern = '[0-9]'
text = 'codegnan 31'

res = re.findall(pattern,text)
print(res)

#print(res.group() if res else "No Match Found")
'''
'''
import re

pattern = '[0-9]'
text = 'codegnan 31'
res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())
'''
'''
import re

pattern = '[a-z]{9}'
text = 'abcdefghi'
res = re.fullmatch(pattern,text)
print(res.group() if res else "No Match Found")
'''

