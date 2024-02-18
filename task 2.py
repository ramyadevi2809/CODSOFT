a=int(input('enter the number1:'))
b=int(input('enter the number2:'))
operator=input("ENTER THE OPERATOR: addition/subtraction/multiplication/division:")
if(operator=="addition"):
    print(a+b)
elif(operator=="subtraction"):
    print(a-b)
elif(operator=="multiplication"):
    print(a*b)
elif(operator=="division"):
    print(a/b)
else:
    print("invalid operator")
