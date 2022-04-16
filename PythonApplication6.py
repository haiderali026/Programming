print("Enter the Number : ")
user=int(input())
if (user < 100):
    while (True):
        print("Enter the Number again : ", end=' ')
        user=int(input())
        if(user>100):
            print("Conguratulation your number is bigger then 100")
            break
else:
    print("Conguratulation your number is bigger then 100")
