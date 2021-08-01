x=int(input())
for i in range(x):
    a=list(map(int,input().split()))
    b=a[0]+a[2]
    c=a[1]+a[3]
    if b==180 or c==180:
        print("YES")
    else:
        print("NO")


##https://www.codechef.com/problems/CYCLICQD
