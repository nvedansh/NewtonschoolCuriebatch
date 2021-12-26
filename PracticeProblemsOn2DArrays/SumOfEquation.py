def equationSum(N) : 
    ans = 0
    for i in range(1, N+1):
        ans += (i+1)**2 - (3*i+1) + i
    return ans