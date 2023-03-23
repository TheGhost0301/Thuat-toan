import math, re

p,w,a,b= map(int, input().split())

m = round(math.log2(p))
t = round(m/w)

def int_to_arr(n):
	n = bin(n)[2:].zfill(8*t)
	b = re.findall('\d{8}', n)
	return [int(i, 2) for i in b]

def int_to_dec(n, f):
	n = bin(n)[2:].zfill(f)
	b = re.findall('\d{8}', n)
	return [int(i, 2) for i in b]

a = int_to_arr(a)
b = int_to_arr(b)

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

