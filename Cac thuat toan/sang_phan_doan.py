def erato(m,n):
	num = [True for i in range(n+1)]
	p = 2
	while (p*p<=n):
		if (num[p] == True):
			print('p=',p)
			for i in range(p*p, n+1, p):
				num[i] = False

		p = p+1
	if m == 1:
		for p in range(2,n+1):
			if num[p] == True:
				print(p,end='  ')
	else:
		for p in range(m,n+1):
			if num[p] == True:
				print(p,end='  ')
               

n = 10
p = 3

count_1 = 0
count_2 = 1
i2 = 2
for i in range(2,n+1):
	print(str(i) + '  ',end='')
	count_1 +=1
	if count_1 == p and i != n :
		print('||',end='')
		count_1 = 0
		count_2+=1
print('')

for i in range(1,count_2+1):
	print('Xet doan {} :'.format(i))
	if i != count_2 :
		erato(i2,i2+p-1)
	else:
		erato(i2,n)
	i2 = i2 + p

# erato(2,n)