import re

line = "[sssss](x,x),[ ](x,x),[sssss](x,x)";

searchObj = re.findall(r'\[(.+?)\]\((.+?)\)', line)

searchObj1 = re.findall(r'\[\]\((.+?)\)', line)

for obj in searchObj:
    print(obj)

