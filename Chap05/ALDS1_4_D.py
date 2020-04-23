n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]

# k台以内のトラックで運べる荷物の個数
# P: ひとつのトラックに積載できる最大量
def check(P):
	i = 0
	for j in range(k):
		s = 0
		while s + w[i] <= P:
			s += w[i]
			i += 1
			if i == n:
				return n
	return i

left = 0
right = 10000 * 10000
while right - left > 1:
	mid = (left + right) // 2
	v = check(mid)
	if v >= n:
		right = mid
	else:
		left = mid

print(right)