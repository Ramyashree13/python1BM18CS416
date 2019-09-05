#program2a

def find(lis,key):
    for i in lis:
        if(i==key):
            print("key found")
            return True
    print("key not found")
    return False

lis=[1,2,3,4,5]
key=int(input("enter the key value"))
value=find(lis,key)
print(value)

#program 2b


def str1(sentence):
    list1=(sentence.split(" "))
    new=""
    for i in list1[::-1]:
        new=new+" "+i
    print(new)
        
sentence=input("enter the string")
str1(sentence)


def str2(sentence):
    list1=sentence.split(" ")
    word=[word1[::-1] for word1 in list1]
    sent=" ".join(word)
    print(sent)
        
sentence=str(input("enter the string"))
str1(sentence)

