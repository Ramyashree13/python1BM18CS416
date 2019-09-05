def find_divisors(lis,n):
    for i in range(1,n+1):
        if(n%i)==0 :
            lis.append(i)
    return lis
n=int(input("enter a number to find its divisors"))
lis=[]
lis=find_divisors(lis,n)
print(lis)
