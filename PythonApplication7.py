n=18
guesse=5
print("Your total lifes : 5")
while(True):
    print("Enter the Number : ",end=' ')
    user=int(input())
    if(user>n):
        print("Your Number is greater ")
        guesse-=1
        print("Your life remaning is : ",guesse)
    elif(user<n):
        print("Your Number is smaller ")
        guesse-=1
        print("Your life remaining is : ",guesse)
    elif(user==n):
        print('\n')
        print("************YOU-WON**********")
        print("Congrats you found the number ")
        print("Your remaining lifes : ",guesse)
        break
    if(guesse==0):
        print('\n')
        print("YOU-LOSE")
        print("Your are out of life")
        print("Your remaining lifes : ",guesse)
        break