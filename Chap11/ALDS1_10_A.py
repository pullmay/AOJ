# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/10/ALDS1_10_A
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())

def fib_memo(n):
	dp = [-1] * (n + 1)
	
	def fib(n):
		if n == 0 or n == 1:
			return 1
		if dp[n] != -1:
			return dp[n]
		dp[n] = fib(n - 1) + fib(n - 2)
		return dp[n]
	return fib(n)

print(fib_memo(n))

stop = time.time()

print('elapsed: {}'.format(stop - start))

# ループ
def fib_loop(n):
	F = [-1] * (n + 1)
	F[0], F[1] = 1, 1
	for i in range(2, n + 1):
		F[i] = F[i - 1] + F[i - 2]
	return F[n]

print(fib_loop(n))

# 配列が欲しい場合
def fib_array(n):
	F = [-1] * (n + 1)
	F[0], F[1] = 1, 1
	for i in range(2, n + 1):
		F[i] = F[i - 1] + F[i - 2]
	return F
