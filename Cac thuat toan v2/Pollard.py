n = int(input())

a = 2
b = 2
def gcd(a,b): 
	A = a
	B = b
	while(B>0):
		R = A % B
		A = B
		B = R 
	return A

print('-'*64)
print('|'+' '*19+'a',end='|')
print(' '*19+'b',end='|')
print(' '*19+'d',end='|'+'\n')

while (True):
	print('-'*64)

	a = (a**2 + 1)%n
	b = ((b**2 + 1)**2 + 1)%n
	d = gcd(a-b,n)
	print('|',end='')
	print('{}|'.format(a).rjust(21),end='')
	print('{}|'.format(b).rjust(21),end='')
	print('{}|'.format(d).rjust(21))

	if 1 < d and d < n :
		print('-'*64)
		print('Thua so khong tam thuong cua {} la'.format(n),d)
		break
	if d == n :
		print('Khong tim thay')
		break