import math, re

p,w= map(int, input().split())
a = [int(k) for k in input().split()]
b = [int(k) for k in input().split()]

def int_to_dec(n, f):
	n = bin(n)[2:].zfill(f)
	b = re.findall('\d{8}', n)
	return [int(i, 2) for i in b]

def solve(a, b, w, p):
	a.reverse()
	b.reverse()
	m = round(math.log2(p))
	t = round(m/w)

	c = [0 for i in range(2*t)]
	
	for i in range(t):
		u = 0
		for j in range(t):
			uv = c[i + j] + int(a[i])*int(b[j]) + u
			[u, v] = int_to_dec(uv, 16)
			c[i + j] = v
		c[i + t] = u
	return c[::-1]

if __name__ == '__main__':
	print('c=a.b='+str(solve(a, b, w, p)).replace(',','   '))

