n = int(input().strip())
while(n>9):
    p = n
    sum=0
    while(p>0):
        sum+=p%10
        p//=10
    n=sum

print(n)