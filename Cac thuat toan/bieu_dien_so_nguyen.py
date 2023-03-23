import math
 
p, w, a = map(int, input().split())

def A(a,p,w):
	m = ceil(math.log2(p))
	t = ceil(m / w)
	lst = []
	tg = a
	for i in range(t-1,-1,-1):
		x = tg // pow(2,(w*i))
		lst.append(x)
		tg = tg % pow(2,(w*i))
	return lst

print('A=',str(A(a,p,w)).replace(',','  '))



