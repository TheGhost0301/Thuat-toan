import math

def gcd( a, b) :
    if (a < b) :
        return gcd(b, a)
    if (a % b == 0) :
        return b
    return gcd(b, a % b)

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def carmichael(n):
	if (is_prime(n)):
		return 0
	
	b = 2
	while b<n :
		if (gcd(b, n) == 1) :
			if (pow(b, n - 1, n) != 1) :
				return 0
		b = b + 1
	return 1


t = int(input())

for i in range(t):
	n = int(input())

	if carmichael(n):
		print('{} la so Carmichael'.format(n))
	else:
		print('{} khong phai so Carmichael'.format(n))
