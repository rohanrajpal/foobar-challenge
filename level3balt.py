def solution(n):
	dp = [[0 for i in range(205)] for j in range(205)]
	dp[0][0] =1
	for j in range(1,201):
		for i in range(0,201):
			dp[i][j] += dp[i][j-1]
			if i >= j:
				dp[i][j] += dp[i-j][j-1]
	return dp[n][200]-1

print(solution(200))