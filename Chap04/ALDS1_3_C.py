from collections import deque

n = int(input())

com = []

for i in range(n):
	# c, v = map(str, input().split())
	c = input().split()
	# v = int(v)
	if len(c) == 1:
		com.append(c)
	else:
		com.append([c[0], int(c[1])])

command = ['insert', 'delete', 'deleteFirst', 'deleteLast']

d = deque([])

for e in com:
	if e[0] == command[0]:
		d.appendleft(e[1])
	elif e[0] == command[1]:
		if e[1] in d:
			d.remove(e[1])
	elif e[0] == command[2]:
		d.popleft()
	elif e[0] == command[3]:
		d.pop()

# print(d)

print(*list(d))