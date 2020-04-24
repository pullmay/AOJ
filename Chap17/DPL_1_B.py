N, W = map(int, input().split())
items = [[0, 0]]

for i in range(N):
	v, w = map(int, input().split())
	items.append([v, w])

# dp table (W + 1) * (N + 1)
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
	for w in range(1, W + 1):
		# print(dp)
		if items[i][1] <= w:
			dp[i][w] = max(dp[i-1][w], dp[i-1][w-items[i][1]] + items[i][0])
		else:
			dp[i][w] = dp[i-1][w]

# print(dp)
print(dp[N][-1])