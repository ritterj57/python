def cycle(n):
    if n ==0:
        return 1
    if n%2 == 0:
        return cycle(n-1)+1
    else:
        return 2*cycle(n-1)
leng= int(input())
out = []
for i in range(0,leng):
    out.append(cycle(int(input())))
for i in range(len(out)):
    print out[i]
