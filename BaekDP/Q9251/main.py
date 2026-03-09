fir_arr = list(input())
sec_arr = list(input())

dp = [[0]*(len(sec_arr)+1) for i in range(len(fir_arr)+1)]

for i in range(len(fir_arr)):
    for j in range(len(sec_arr)):
        if fir_arr[i] == sec_arr[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[len(fir_arr)][len(sec_arr)])
