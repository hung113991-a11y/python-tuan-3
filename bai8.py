a = float(input())
if a>0 and a<=1:
    cuoc=a*20000
    print(cuoc)
elif a<=5:
    cuoc=(a-1)*30000+20000
    print(cuoc)
elif a<=10:
    cuoc=(a-5)*50000+30000+20000
    print(cuoc)