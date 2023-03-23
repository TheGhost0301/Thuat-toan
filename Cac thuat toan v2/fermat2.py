n = int(input())
t = int(input())
x = [int(k) for k in input().split()]

def fermat(n,t,x):
	check = 1
	for i in range(0,t):
		a = x[i]
		r = pow(a,n-1,n)
		if r != 1:
			check = 0
			print('Co so a={}: Hop so'.format(a))
		else:
			print('Co so a={}: Nguyen to'.format(a))


	if check == 0:
		print('{} la hop so'.format(n))
	else:
		print('{} co the la nguyen to'.format(n))

print('Kiem tra so nguyen n={}:'.format(n))

fermat(n,t,x)



