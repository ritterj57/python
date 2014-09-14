def pal(lword):
    out = [ord(char) - 96 for char in lword]
    if len(out)%2==1:
        maxi = int(len(out)/2)
        
    else:
        if out[int(len(out)/2)-1] < out[int(len(out)/2)]:
            maxi = int(len(out)/2) -1
        else:
            maxi = int(len(out)/2) 
    return out, maxi
def cpal(lword):
    out, maxi = pal(lword)
    maxim = out[maxi]
    outval = 0
    for i in range(0, len(out)):
        if out[i]> maxim:
            outval += out[i]-maxim
            out[i] = maxim  
    return out, outval

def dpal(olist,maxi):
    out = []
    

print (cpal('abba'))
    
