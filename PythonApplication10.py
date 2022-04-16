rows =0
print("Enter the Number of Rows : ",end='')
rows=int(input())
# outer loop
for i in range(1, rows+1 ):
    # inner loop
    for j in range(1, i+1):
        print("*", end=" ")
    print('')