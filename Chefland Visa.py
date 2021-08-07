x=int(input())
for i in range(x):
    y=list(map(int,input().split()))
    if (y[0] <= y[1] and y[2] <= y[3] and y[4] >= y[5]):
        print("YES")
    else:
        print("NO")

##https://www.codechef.com/problems/VISA
