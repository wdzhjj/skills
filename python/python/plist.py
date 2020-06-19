from biplist import *
from datetime import datetime


# appname = "tets"
# app = "xxxx.ipa"
# version = 'v1.1'


# plist = readPlist("plist.plist")
# print(plist)
# print("=====================")

# print("=====================")


# plist['items'][0]['assets'][0]['url'] = "https://appsign.hmset.com/xx/"+app

# plist['items'][0]['metadata']['title'] = appname

# plist['items'][0]['metadata']['bundle-version'] = version

# writePlist(plist,app+'.plist')


f = open("pp.plist")
content = f.read()
print(content)

f2 = open("test.plist",'w')
str = '12345'
f2.write(content %(str, str, str, str, str, str) )  