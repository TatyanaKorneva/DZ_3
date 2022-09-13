import random
n=int(input())
l=[]
random.uniform
for i in range(1, n+1):
    l.append(random.uniform(-n, n+1))
print(max(l)%1-min(l)%1)

