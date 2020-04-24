n, m = map(int, input().split())
c = [0] + list(map(int, input().split()))

INF = 1 << 29

# dp table 
NMAX = 500000
dp = [INF] * (NMAX + 1)

dp[0] = 0

for i in range(1, m + 1):
	for j in range(c[i], n + 1):
		dp[j] = min(dp[j], dp[j-c[i]] + 1)

print(dp[n])
