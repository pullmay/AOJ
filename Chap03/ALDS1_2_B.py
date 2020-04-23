# Selection Sort

n = int(input())
A = list(map(int, input().split()))

# A = [5, 6, 4, 2, 1, 3]

def selectionSort(A):
	n = len(A)
	cnt = 0
	for i in range(n - 1):
		minj = i
		for j in range(i, n):
			if A[j] < A[minj]: minj = j
		A[i], A[minj] = A[minj], A[i]
		# print(A)
		if i != minj: cnt += 1
	return cnt

cnt = selectionSort(A)

print(*A)
print(cnt)
