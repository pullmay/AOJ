n = int(input())
a = list(map(int, input().split()))

from math import gcd

def lcm(a, b):
	return a * b // gcd(a, b)


tmp = lcm(a[0], a[1])
for i in range(2, n):
	tmp = lcm(tmp, a[i])

print(tmp)
