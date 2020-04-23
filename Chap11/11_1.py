# 配列の要素を任意に選んで、その和をmにできるか

n = int(input())
A = list(map(int, input().split())) #n
q = int(input())
m = list(map(int, input().split())) #q

# A = [1, 5, 7]
# n = len(A)
# m = 8
NMAX = n + 1
MMAX = 2001
# dp[NMAX, MMAX]
dp = [[False] * (MMAX + 1) for _ in range(NMAX + 1)]
# dp = [[False] * (20) for _ in range(20)]

# print(dp)

def solve(i, m):
	if dp[i][m]:
		return dp[i][m]
	if m == 0:
		dp[i][m] = True
	elif i >= n:
		dp[i][m] = False
	elif solve(i + 1, m):
		dp[i][m] = True
	elif solve(i + 1, m - A[i]):
		dp[i][m] = True
	else:
		dp[i][m] = False

	return dp[i][m]


# print(solve(0, 8)) # True
# print(solve(1, 8))
# print(solve(2, 8))
# print(solve(3, 8))


# 二次元配列の初期化
# row = 5 # 行
# col = 8 # 列
# init = [[0] * col for i in range(row)] # 5行8列
# print(init)

# 出力
for i in range(q):
	if solve(0, m[i]):
		print('yes')
	else:
		print('no')