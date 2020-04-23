# コッホ曲線
from math import sin, cos, tan, pi

n = int(input())

def koch(n, a, b):
	if n == 0:
		return
	s = [0, 0]
	t = [0, 0]
	u = [0, 0]
	th = pi * 60 / 180

	s[0] = (2 * a[0] + 1 * b[0]) / 3
	s[1] = (2 * a[1] + 1 * b[1]) / 3
	t[0] = (1 * a[0] + 2 * b[0]) / 3
	t[1] = (1 * a[1] + 2 * b[1]) / 3
	u[0] = (t[0] - s[0]) * cos(th) - (t[1] - s[1]) * sin(th) + s[0]
	u[1] = (t[0] - s[0]) * sin(th) + (t[1] - s[1]) * cos(th) + s[1]
	
	koch(n - 1, a, s)
	# print(s[0], s[1])
	print('{:.8f} {:.8f}'.format(s[0], s[1]))
	koch(n - 1, s, u)
	# print(u[0], u[1])
	print('{:.8f} {:.8f}'.format(u[0], u[1]))
	koch(n - 1, u, t)
	# print(t[0], t[1])
	print('{:.8f} {:.8f}'.format(t[0], t[1]))
	koch(n - 1, t, b)

a = [0.0, 0.0]
b = [100.0, 0.0]
# print(a[0], a[1])
print('{:.8f} {:.8f}'.format(a[0], a[1]))
koch(n, a, b)
# print(b[0], b[1])
print('{:.8f} {:.8f}'.format(b[0], b[1]))