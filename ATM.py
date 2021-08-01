x,y=input().split()
x=int(x)
y=float(y)
if x<=y-0.5:
    if x%5==0:
        print(y-x-0.5)
    else:
        print(y)
else:
    print(y)
