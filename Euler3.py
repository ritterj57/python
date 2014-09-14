import math

top = 600851475143
cil=math.ceil(math.sqrt(600851475143))
mxx=0

options = []
for i in range(1, cil):
    options.append(i)
mxx = 0
for e in options:
    if top%e == 0:
        top = top / e
        mxx = e
print (max(top, mxx))
    
