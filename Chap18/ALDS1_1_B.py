# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_B

x, y = map(int, input().split())

from math import gcd

print(gcd(x, y))