options = [i for i in range(100, 999)][::-1]

def ispal(n,m):
    pal = n*m
    pal = str(pal)
    for i in range(0,len(pal)):
        if pal[i] != pal[-i-1]:
            return False
    else:
        return True
    

def hipal(plist,qlist):
    pallist=[]
    for p in plist:
        for q in qlist:
            if ispal(p,q):
                pallist.append(p*q)
    return max(pallist)
                
    return 1
    
print (hipal(options,options))

