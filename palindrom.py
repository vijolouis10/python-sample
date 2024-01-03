n=int(input("enter number:"))


for i in range(0,n+1):
    ans=str(i)[::-1]
    if i==int(ans):
        print(ans)