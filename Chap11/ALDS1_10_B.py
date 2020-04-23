# 行列の乗算回数に関する問題
# 十分に理解してない

n = int(input())

N = 101

p = [0] * N
m = [[0] * N for _ in range(N)]

for i in range(1, n + 1):
	p[i - 1], p[i] = map(int, input().split())

# print(p)

for l in range(2, n + 1):
	for i in range(1, n - l + 2):
		j = i + l - 1
		m[i][j] = float('inf')
		for k in range(i, j):
			m[i][j] = min(m[i][j], m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j])

print(m[1][n])

