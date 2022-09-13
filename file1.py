import random
n=int(input())
l=[]
g=[]
for i in range(1, n+1):
    l.append(i)
random.shuffle(l)
for j in range(len(l)):  
    if j%2>0:
       g.append(l[j])
print(l, g, sum(g))
