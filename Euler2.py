plist=[1,2]
new=0
evenlist = [2]

while new < 4000000:
    new = plist[-1]+plist[-2]
    if new%2==0:
        evenlist.append(new)
    plist.append(new)
smm=0
for e in evenlist:
    smm+=e
print(smm)
    
    
    
