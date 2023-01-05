import re

'''
str='We need to inform him with the latest information'
for i in re.finditer('inform',str):
    loctup=i.span()
    print(loctup)
'''
'''
str='Sat,hat,pat,cat'
allstr=re.findall('[Shpc]at',str)

for i in allstr:
    print(i)
'''
'''

str='Sat,hat, cat,mat,pat'
allstr=re.findall('[^h-c]at',str)

for i in allstr:
    print(i)
(doubt)
'''
'''
str='Pat same and sat saturday'
allstr=re.compile('[s]at')

str=allstr.sub('food',str)
print(str)
'''
'''
str='014-5649-987-78960'

if re.search('\w{3}-\w{4}-\w{3}-\w{5}',str):
    print("no is valid")
'''
'''
str='413 5674,345 8976 9873531098 100'
print("Matches:",len(re.findall('\d{3,4}',str)))
                     
'''
import urllib.request



url=urllib.request.urlopen('https://www.summet.com/dmsi/html/codesamples/addresses.html')
var1=url.read()
var2=var1.decode()

ata=re.findall("\(\d{3}\) \d{3}-\d{4}",var2)
for i in data:
    print(i)










