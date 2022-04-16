print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")
print('\n')
print("Enter the First Value : ", end=' ')
val1=int(input())
print("Enter the Second Value : ", end=' ')
val2=int(input())

print("Enter your Mathamatical operator : ", end=' ')
operator = int(input())
if val1==45 and val2==3 and operator==3:
    print("Here is the result : 555")
elif val1==56 and val2==9 and operator==1:
    print("Here is the result : 77")
elif val1==56 and val2==6 and operator==4:
    print("Here is the result : 4")
elif operator==1:
    print("Here is the result : ",end=' ')
    print(val1+val2)
elif operator==2:
    print("Here is the result : ", end=' ')
    print(val1-val2)
elif operator==3:
    print("Here is the result : ",end=' ')
    print(val1*val2)
elif operator==4:
    print("Here is the result : ",end=' ')
    print(val1/val2)