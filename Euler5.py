import math

alist = [i for i in range(1,21)]

plist =[2,3,5,7,11,13,17,19]

tlist = []

for e in plist:
    tlist.append([e,1])

def factor(n):
    qlist = [i for i in range(2,n)]
    out_list=[]
    for e in qlist:
        if n%e==0:
            out_list.append(e)
    return out_list
print (factor(1))
    
