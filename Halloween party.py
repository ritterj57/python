tests = int(input())
choc = []
for i in range(0, tests):
    choc.append(int(input()))
    
def cut(n):
    if n%2==0:
        return int((n/2)**2)
    else:
        return int(n/2)*(int(n/2)+1)
for e in choc:
    print(cut(e))
    
