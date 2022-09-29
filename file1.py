from ctypes.wintypes import MSG
from unittest import result
from logger import logger

results=[]
with open ("./1/aaa/students.txt","r") as f:
    lst=[]
    vallst=[]
    for index,rowstr in enumerate(f):
        #print(index,":",rowstr.strip())
        if index==0:
           lst= rowstr.strip().split(',')
        else:
            tmpdict={}
            vallst=rowstr.strip().split(',')
            tmpdict=dict(zip(lst,vallst))
            results.append(tmpdict)
print(results)