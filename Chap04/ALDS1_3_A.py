A = list(input().split())

op = ['+', '-', '*']

stack = []

for v in A:
	if v not in op:
		stack.append(v)
	elif v in op:
		tmp1 = int(stack.pop())
		tmp2 = int(stack.pop())
		if v == '+':
			stack.append(tmp2 + tmp1)
		elif v == '-':
			stack.append(tmp2 - tmp1)
		elif v == '*':
			stack.append(tmp2 * tmp1)

print(stack[0])