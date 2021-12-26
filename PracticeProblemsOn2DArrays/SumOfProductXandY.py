#3 test cases will fail, NS portal problem
t = int(input().strip())
for testcase in range(t):
    n = int(input().strip())
    ans = 0
    for i in range(1, n+1):
        ans += i*(n // i)
    print(ans)