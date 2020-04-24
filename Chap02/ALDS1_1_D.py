n = int(input())
R = [int(input()) for _ in range(n)]

minv = R[0]
maxv = - 1 << 30 # 十分に大きい数

print(maxv)

for j in range(1, n):
	maxv = max(maxv, R[j] - minv)
	minv = min(minv, R[j])

print(maxv)
