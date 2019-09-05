import string
import random

str1=string.printable
n=random.randint(10,15)
print(n)
for i in range(n):
    print(str1[random.randint(0,n)],end=" ")
