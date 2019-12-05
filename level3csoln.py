from fractions import gcd

def answer(m):
    r = len(m)
    c = len(m[0])
    
    t_states = []
    nt_states = []
    
    for r1 in range(r):
      m[r1][r1] = 0
      if sum(m[r1]) == 0:
        t_states.append(r1)
      else:
        nt_states.append(r1)
    
    L = len(nt_states)
    for i in range(L):
        a=nt_states[i]
        for j in range(L):
            if i != j:
              b=nt_states[j]        
              m[b]=gcf(m[a],m[b],a,b)
    
    output=[]
    tot=sum((m[0][i] for i in t_states))
    if tot == 0:
        output=[1]*len(terms)
        output.append(len(terms))
    else:
      output = [m[0][i] for i in t_states] + [tot]
    return output
    
    

    
def gcf(v1,v2,i1,i2):
    tot=sum(v2)
    n = len(v1)
    out = [0]*n
    
    gc = 0
    for i in range(n):
      if i == i1 or i == i2:
        continue
      out[i] = v1[i2]*v2[i]
      out[i] += tot*v1[i]
      gc = gcd(gc,out[i])
      
    for i in range(n):
        out[i] /= gc
      
    return out

matrix2= [[0, 1, 0, 0, 0, 1], 
[4, 0, 0, 3, 2, 0], 
[0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0]]

print(answer(matrix2))