# Thuật toán trừ chính xác bội.  c = a - b mod2𝑊𝑡
import math 

p, w, a, b = map(int, input().split())

m = round(math.log2(p))
t = round(m/w)
def A(a,p,w):
		lst = []
		tg = a
		for i in range(t-1,-1,-1):	
			x = tg // pow(2,(w*i))
			lst.append(x)
			tg = tg % pow(2,(w*i))
		return lst
a = A(a,p,w)
b = A(b,p,w)
def slove(a, b, w, t):
	c = []
	e = 0
	for i in range(t-1,-1,-1):
		d = int(a[i]) - int(b[i]) - e
		if(d < 0): 
			d += pow(2,w)
			e = 1
		else: e = 0
		x = d%pow(2,w)
		c.append(x)
	return e, str(c[::-1]).replace(', ','   ')

print('c=a-b='+str(slove(a,b,w,t)).replace("'",""))
	