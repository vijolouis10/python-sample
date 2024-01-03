n=int(input("enter the number: "))
for a in range(1,n):
    for b in range(0,n-a):
        print(""*b,end=" ")
    for c in range(a,0,-1):
        print("*",end=" ")   
    print()     

for i in range(n,0,-1):  
    for k in range(n,i,-1):
        print(""*k,end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()    

     