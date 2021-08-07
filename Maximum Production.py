t=int(input())
for i in range(t):
    d,x,y,z=map(int,input().split())
    a=(7*x)
    b=((y*d))+(z*(7-d))
    c=max(a,b)
    print(c)
