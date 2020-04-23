from bisect import bisect_left

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

S.sort() # 昇順にソート

cnt = 0

for i in range(q):
	idx = bisect_left(S, T[i])
	if idx < n and S[idx] == T[i]:
		cnt += 1

print(cnt)

# binaryserch
def binarySearch(A, key):
	left, right = 0, len(A)
	while left < right:
		mid = (left + right) // 2
		if A[mid] == key:
			return True
		elif key < A[mid]:
			right = mid
		else:
			left = mid + 1
	return False

cnt = 0
for i in range(q):
	if binarySearch(S, T[i]): cnt += 1

print(cnt)