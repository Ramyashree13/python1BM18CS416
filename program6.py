class py_solution:
    def is_valid(self,str1):
        stack,pchar = [],{"(":")","{":"}","[":"]"}
        for parenthese in str1:
            if parenthese in pchar:
                    stack.append(parenthese)
            elif len(stack)==0 or pchar[stack.pop()] !=parenthese:
                    return False
        return len(stack)==0


str1=input("enter the string")
x=py_solution()
res=x.is_valid(str1)
print(res)
