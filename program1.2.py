def fib():
    first=0
    second=1
    a=int(input("enter the number"))
    print(first,second)
    for i in range(a-2):
        num=first+second
        first=second
        second=num
        print(num)

fib()
