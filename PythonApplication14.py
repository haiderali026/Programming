import random
lst=["snake","gun","water"]
option=0
i=0
option='y'
flag=True
print("Enter Your Name : ",end=' ');
profile=input()
while(option=='y'):
    i=0
    player_score=0
    computer_score=0
    print("How many games you want to Play : ",end=' ')
    g=int(input())
    print("                ******New-Game******")
    while(i<g):
        i+=1
        choice=random.choice(lst)
        print("Your options are ( snake , gun , water ) ")
        print("Enter Your Move :",end=' ')
        option=input()
        if(option=="snake"and choice=="water"):
            player_score+=10
        elif(option=="gun"and choice=="snake"):
            player_score+=10
        elif(option=="water"and choice=="gun"):
            player_score+=10
        elif(option=="snake"and choice=="gun"):
            computer_score+=10
        elif(option=="gun"and choice=="water"):
            computer_score+=10
        elif(option=="water"and choice=="snake"):
            computer_score+=10
        elif(option==choice):
            print("Match Tied ")
        else:
            print("Your Input is not valid....!")
            print("Try Again")
            i-=1
            flag=False
            continue
        if(flag==True):
            print("Computer Move : ",end=' ')
            print(choice)
        flag=True
    if(player_score>computer_score):
        print("Player Name : ",profile)
        print("You Won")
        print("Your Score : ",player_score, " VS ","Computer Score : ",computer_score)
    else:
        print("Player Name : ",profile)
        print("You Lose")
        print("Computer Score : ",computer_score," VS ","Your Score : ",player_score)
    print("Dp you want to contine (y/n) : ",end=' ')
    option=input()