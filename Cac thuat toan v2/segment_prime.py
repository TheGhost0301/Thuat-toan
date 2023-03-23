import math

n = 11
p = 3

def fillPrimes(chprime, high):
    ck = [True]*(high+1)

    for i in range(2, high+1):
        if ck[i]:
            for j in range(i*i, high+1, i):
                ck[j] = False             
 
    for k in range(2, high+1):
        if ck[k]:
            chprime.append(k)

def segmentedSieve(low, high):
     
    chprime = []
    fillPrimes(chprime, high)
    print(chprime)
    prime = [True] * (high-low + 1)

    for i in chprime:
        lower = (low//i)
        if lower <= 1:
            lower = i+i
        elif (low % i) != 0:
            lower = (lower * i) + i
        else:
            lower = lower*i
        for j in range(lower, high+1, i):
            prime[j-low] = False
              
        for k in range(low, high + 1):
            if prime[k-low]:
                print(k, end=" ")

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
print('\n')
for i in range(1,count_2+1):
    print('\nXet doan {} :'.format(i))
    if i != count_2 :
        segmentedSieve(i2,i2+p-1)
    else:
        segmentedSieve(i2,n)
    i2 = i2 + p


# segmentedSieve(2,n)


