from bisect import bisect_left

n = int(input())
A = [int(input()) for _ in range(n)]


def LIS(arr):
	dp = [arr[0]]
	for i in arr[1:]:
		if dp[-1] < i:
			dp.append(i)
		else:
			dp[bisect_left(dp, i)] = i
	return len(dp)

print(LIS(A))