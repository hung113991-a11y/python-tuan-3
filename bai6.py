a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < 1 or b < 1 or c < 1 or d < 1 or a > 8 or b > 8 or c > 8:
    print("NO")
elif a==c and (b>d or b<d):
    print("YES")
elif b==d and (c>a or c<a):
    print("YES")
else:
    print("NO")