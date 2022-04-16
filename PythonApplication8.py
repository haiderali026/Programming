print("Enter the Number of Lines : ",end=' ')
n=int(input())
print("Enter the Side of Shape : (0 or 1) : ",end=' ')
side=int(input())
flag=bool(side)
i=0
def new_func():
    j=0
    return j

while(i<=n):
    j = new_func()
    if side:
        while(j<=i):
            print('*',end='')
            j=j+1
        print('\n')
        i=i+1
    else:
        j=n
        i=0
        k=n
        while(i<=k):
            j=n
            while(j>=0):
                print('*',end='')
                j-=1
            print('\n')
            n-=1
            i+=1