nlines = int(input())
llines = []

for i in range(0, nlines):
    llines.append(str(input()))
olines =[]
for j in range(0,len(llines)):
    temp = set()
    for i in range(0,len(llines[j])):
        temp.add(llines[j][i])
    olines.append(temp)
    
print(len(set.intersection(*olines)))
