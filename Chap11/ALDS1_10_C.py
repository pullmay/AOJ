# X = input()
# Y = input()

# c = [[0] * 1001 for _ in range(1001)]

# m = len(X)
# n = len(Y)

# maxl = 0

def LCS(X, Y):
	global maxl # 重要
	for i in range(m):
		for j in range(n):
			if X[i] == Y[j]:
				c[i][j] = c[i-1][j-1] + 1
			else:
				c[i][j] = max(c[i-1][j], c[i][j-1])
			maxl = max(maxl, c[i][j])
	return maxl

# print(LCS(X, Y))


# 入力
q = int(input())

while q > 0:
	X = input()
	Y = input()
	c = [[0] * 1001 for _ in range(1001)]
	m, n = len(X), len(Y)
	maxl = 0
	print(LCS(X, Y))
	q -= 1