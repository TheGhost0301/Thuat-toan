import math

def erato(n):
    
    mark = [True]*(n+1) 

    x = [i for i in range(2,n+1)]
    print(str(x).replace(',',' ')[1:-1])
    for i in x: 
        print('p={}'.format(i))
        if mark[i]:
            for j in range(i*i,n+1,i):
                mark[j]=False 
                if j in x:
                    x.remove(j)
        print(str(x).replace(',',' ')[1:-1])
        

    primes=[]
    for i in range(2,n+1):
        if mark[i]: 
            primes.append(i) 
    print('Cac so nguyen to <={} la:'.format(n) +'\n'+ str(primes).replace(',',' ')[1:-1])

# n = int(input())
n = 4

print('Liet ke cac so nguyen tu 2 den {}'.format(n))

erato(n)