#Euclide a mod b
import math

a = int(input())
b = int(input())

def Euclide(a,b):

	if b == 0:
		return [a,1,0]
	x2 = 1
	x1 = 0
	y1 = 1
	y2 = 0
	while b > 0:
		q = math.floor(a / b)
		r = a - q*b
		x = x2 - q*x1
		y = y2 - q*y1
		a = b
		b = r
		x2 = x1
		x1 = x
		y2 = y1
		y1 = y
		print(q,r,x,y,a,b,x2,x1,y2,y1)
	return [a,x2,y2]

[d,x,y] = Euclide(a,b)
print(d,x,y)








