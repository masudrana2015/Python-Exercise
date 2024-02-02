k = ""

def reverse_str(n,l):
    global k
    if n < l-1:
        reverse_str(n+1,l)
        
    k = k + s[n]
    return k  
    

s="Bongodev"

t=reverse_str(0,len(s))
print(t)
