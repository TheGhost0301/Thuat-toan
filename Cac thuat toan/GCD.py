
#UCLN
def gcd(a,b): 
	A = a
	B = b
	while(B>0):
		R = A % B
		A = B
		B = R 
	return A


a=int(input())
b=int(input())
print(gcd(a,b))