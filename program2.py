
/* program 2b */
def str1(sentence):
  list1=(sentence.split(" "))
  for i in list1[::-1]:
      print(i)

sentence=str(input("enter the string"))

str1(sentence)
