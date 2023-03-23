import math

def primeFactors(n):
    lst = []
    hkt = []
    for i in range(2,n+1):
        count = 0
        while(n % i == 0):
            count += 1
            n = n / i
            lst.append(i)
        if (count):
            hkt.append(count)
    return lst,hkt  

n = int(input())

x,y = primeFactors(n)
x = list(set(x))

result = []
for i in range(len(x)):
    result.append(str(x[i])+'^'+str(y[i]))

print('n = {} = '.format(n),end='')
print(' + '.join(result))

    