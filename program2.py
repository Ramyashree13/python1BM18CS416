
#program 2b 


def str1(sentence):
  list1=(sentence.split(" "))
  for i in list1[::-1]:
      print(i)

def str2(sentence):
    list1=sentence.split(" ")
    word=[word1[::-1] for word1 in list1]
    sent=" ".join(word)
    print(sent)
        
sentence=str(input("enter the string"))
str1(sentence)

