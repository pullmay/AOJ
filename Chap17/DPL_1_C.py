N, W = map(int, input().split())
items = [[0, 0]]

for i in range(N):
	v, w = map(int, input().split())
	items.append([v, w])

# dp table (W + 1) * (N + 1)
dp = [[0] * (W + 1) for _ in range(N + 1)]

