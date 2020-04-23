n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

def search(A, key):
	n = len(A)
	for i in range(n):
		if A[i] == key:
			return True
	return False

def linearSearch(A, key):
	n = len(A) - 1
	i = 0
	A[n] = key # 番兵
	while (A[i] != key):
		i += 1
	return i != n

cnt = 0
for i in range(q):
	key = T[i]
	if search(S, key):
		cnt += 1

print(cnt)

cnt = 0
for i in range(q):
	key = T[i]
	if linearSearch(S, key):
		cnt += 1

print(cnt)