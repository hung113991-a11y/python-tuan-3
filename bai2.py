a,b,c = list(map(float,input().split()))
x = a
if a==b and b==c:
    print(a)
else:
    if x<b:
        x = b
    if x<c:
        x = c
    print(x)