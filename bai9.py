a = float(input())
b = float(input())
c = float(input())
d = float(input())
if (a==b and c==d) or (b==c and d==a) or (a==c and d==b) or (b==c and d==a):
    print("YES")
else:
    print("NO")