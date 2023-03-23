import math,re

p,w,a,b= map(int, input().split())
m = round(math.log2(p))
t = round(m/w)

def int_to_arr(n):
	n = bin(n)[2:].zfill(8*t)
	b = re.findall('\d{8}', n)
	return [int(i, 2) for i in b]

def arr_to_int(n):
	x = [bin(i) for i in n ]
	y = [j.replace('0b','').zfill(8) for j in x] 
	b = ''.join(y)
	return int(b,2)

a = int_to_arr(a)
b = int_to_arr(b)

def addition(a, b, w, t):
	lst = []
	e = 0
	for i in range(t-1,-1,-1):
		sum = int(a[i])+int(b[i]) + e
		x = sum // pow(2,w)
		if x == 0:
			lst.append(sum)
			e = 0
		else:
			lst.append(sum % pow(2,w))
			e = 1
	return [e,lst[::-1]]

def subtraction(a, b, w, t):
	c = []
	e = 0
	for i in range(t-1,-1,-1):
		d = (a[i]) - (b[i]) - e
		if(d < 0): 
			d += pow(2, w)
			e = 1
		else: 
			e = 0
		x = d%pow(2,w)
		c.append(x)
	return e, c[::-1]


if __name__ == '__main__' :
	[epsilon,c] = subtraction(a,b,w,t)
	p = int_to_arr(p)
	if epsilon == 1:
		e,c = addition(c,p,w,t)
	print(str(c).replace(',','   '))

