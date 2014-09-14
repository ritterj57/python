plist=[]
for i in range(1, 1000):
    if (i%3==0) or (i%5==0):
        plist.append(i)

smm=0

for e in plist:
    smm+=e

print (smm)
