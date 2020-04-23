from collections import deque

n, q = map(int, input().split())
query = []

for i in range(n):
	n, t = map(str, input().split())
	query.append([n, int(t)])

d = deque(query)

ans = []

time = 0
while len(d) > 0:
	tmp = d.popleft()
	if tmp[1] > q:
		res = [tmp[0], tmp[1] - q]
		time += q
		d.append(res)
	else:
		time += tmp[1]
		ans.append([tmp[0], time])
	# print(d)

# print(ans)

for v in ans:
	print(v[0], v[1])