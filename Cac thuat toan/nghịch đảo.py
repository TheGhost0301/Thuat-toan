import math

p = int(input())
a = int(input())

def slove(a,p):
	u = a
	v = p

	x1 = 1
	x2 = 0

	while u != 1:
		q = math.floor(v/u)
		r = v - q*u
		x = x2 - q*x1
		v = u
		u = r 
		x2 = x1
		x1 = x

	return x1

print(slove(a,p))