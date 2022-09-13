n = int(input())
l = [0,1]
g = [1]
for i in range(2,n+1):
    l.append(l[i-2]+l[i-1])
    g.append((-1)**(i+1)*(l[i-2]+l[i-1]))
g.reverse()
print(g+l)


