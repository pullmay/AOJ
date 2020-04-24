n = int(input())

def prime_factor(n):
	factor = []
	for i in range(2, int(n ** 0.5) + 1):
		while (n % i == 0):
			factor.append(i)
			n //= i
	if n != 1:
		factor.append(n)
	return factor

def Euler_phi(n):
	divisors = prime_factor(n)
	divisors = set(divisors)
	res = n
	for factor in divisors:
		res = res * (factor - 1) // factor
	return res

print(Euler_phi(n))