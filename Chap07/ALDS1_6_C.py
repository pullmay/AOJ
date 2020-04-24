# Quick Sort
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/6/ALDS1_6_C
# TLE with python...

n = int(input())
Card = []

for i in range(n):
	mark, num = map(str, input().split())
	Card.append([mark, int(num)])

# print(Card)

Card_copy = Card[:]

# print(Card_copy)

# 二次元配列用に変形
def partiton(A, p, r):
	x = A[r][1]
	i = p - 1
	for j in range(p, r):
		if A[j][1] <= x:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i + 1], A[r] = A[r], A[i + 1]
	return i + 1

# 二次元配列用に変形
def bubbleSort(A):
	n = len(A)
	for i in range(n):
		for j in range(n - 1, 0, -1):
			if A[j][1] < A[j - 1][1]:
				A[j], A[j - 1] = A[j - 1], A[j]
	return 0

def quickSort(A, p, r):
	if p < r:
		q = partiton(A, p, r)
		quickSort(A, p, q - 1)
		quickSort(A, q + 1, r)

def is_stable(A, B):
	for i in range(len(A)):
		if A[i][0] != B[i][0]:
			return False
	return True

quickSort(Card, 0, n - 1)
bubbleSort(Card_copy)

# 出力
print('Stable') if is_stable(Card, Card_copy) else print('Not stable')
for i in range(n):
	print(*Card[i])
