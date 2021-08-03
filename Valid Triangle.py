x=int(input())
for i in range(x):
    a=list(map(int,input().split()))
    if(a[0]+a[1]+a[2]==180):
        print("YES")
    else:
        print("NO")


##https://www.codechef.com/problems/FLOW013
