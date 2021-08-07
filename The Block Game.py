x=int(input())
for i in range(x):
    a=input()
    b=a[::-1]
    if b==a:
        print("wins")
    else:
        print("loses")

##https://www.codechef.com/problems/PALL01

##a[::-1] - This will reverse the number. GOOGLE it to understand more.
