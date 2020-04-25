# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_C

n = int(input())
A = [int(input()) for _ in range(n)]

# 素数判定 O(n ** 0.5)
def is_prime(n):
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return n != 1

cnt = 0
for v in A:
	if is_prime(v): cnt += 1

print(cnt)