import math 

p, w, a, b = map(int, input().split())

m = ceil(math.log2(p))
t = ceil(m/w)

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
	return e,str(lst[::-1]).replace(', ','   ')

print('A+B='+str(slove(a,b,w,t)).replace("'",""))






