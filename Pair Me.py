x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    if a==b+c or b==a+c or c==a+b:
        print('YES')
    else:
        print('NO')


##https://www.codechef.com/problems/SUMPOS
