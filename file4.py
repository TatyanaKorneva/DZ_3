n = int(input())
f = ''
while n > 0:
    f = str(n%2)+f
    n = n//2
print(f)


