text_file = open("euler 8 number.txt", "r")
euler=''

for aline in text_file:
    euler +=aline

ler = euler.splitlines()
for e in ler:
    euler += str(e)
enums =[]

for j in range(4):
    enums+=[euler[i+j:i+13+j]for i in range(0,len(euler))]

print(enums)
    
    


    


