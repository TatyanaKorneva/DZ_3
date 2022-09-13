n=int(input())
l=[]
g=[]
for i in range(1, n+1):
    l.append(i)
for i in range(len(l)-len(l)//2):
    g.append(l[i]*l[-i-1])
print(l, g, sep='\n')