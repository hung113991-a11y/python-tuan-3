a,b,c = map(float,input().split())
if(a+b>c or b+c>a or c+a>b):
    if a==b and b==c:
        print("Tam Giác Đều")
    elif a==b or b==c or c==a:
        print("Tam Giác Cân")
    elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
            print("Tam Giác Vuông")
    else:
        print("Tam Giác Thương")