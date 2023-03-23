n = int(input())
a = int(input())
k = int(input())

Kx = bin(k)[2:]
t = len(Kx)
print('Chuyen {} sang nhi phan: {}'.format(k,Kx))

b = 1
A = a
print('Dat A=a={}'.format(A))

if Kx[t-1] == '1':
	b = a
	print('- k_{}=1'.format(0),end=', ')
	print('dat b=a={}'.format(a))

lst = Kx[::-1]

for i in range(1,t):
	A = (A**2)%n
	print('Dat A=A^2 mod {}={}'.format(n,A))
	if lst[i] == '1':
		b = (A*b)%n
		print('- k_{} =1'.format(i),end=', ')
		print('dat b=b*A mod {}={}'.format(n,b))

print('=> {}^{} mod {}={}'.format(a,k,n,b))	



	