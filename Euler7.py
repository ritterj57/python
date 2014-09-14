prime = [2]
num = 2
while len(prime)< 10001:
    num+=1
    for e in prime:
        if num%e ==0:
            break
    else:
        prime.append(num)
print (prime[-1])
