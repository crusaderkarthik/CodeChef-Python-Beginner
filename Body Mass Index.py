x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    c=(a/(b*b))
    if c<=18:
        print("1")
    elif c>19 and c<24:
        print("2")
    elif c>25 and c<29:
        print("3")
    else:
        print("4")


##https://www.codechef.com/problems/BMI
