def find_s_r(n):
    s = 1
    while True:
        if (n-1)%(2**s) != 0:
            break
        s+=1
    s = s-1
    r = (n-1)//(2**s)
    return s,r

def Miler_Rabin(n,a,b):
    s, r = find_s_r(n)
    print(f'Kiem tra so nguyen n={n}:')
    print('{}-1 = 2^{}.{}'.format(n,s,r))
    check = []
    for i in range(a+1,b):
        res = True
        a = i
        print(f'Co so a= {a}:')
        y = pow(a,r,n)

        if y != 1 and y != n-1:
            print(f'y= {y} => (y!=1)&&(y!=n-1)')
            j = 1
            print(" "*3 + "j=1")
            print(" "*3 + f'j=1, y={y} =>(j<=s-1)&&(y!=n-1)')

            while j <= s - 1 and y != n - 1:
                y = pow(y,2,n)
                j = j + 1
                if j <= s - 1 :
                    if y == 1 :
                        print(" "*3+f'y={y}')
                        print('Ket qua: Hop so')
                        res = False
                        break
                    print(" "*3 + f'j={j}, y={y} =>(j<=s-1)&&(y!=n-1)')
            if y != n - 1 and j > s - 1:
                if y == 1 :
                    print(" "*3+f'y={y}')
                else :
                    print(f'y = {y} => y!=n-1')
                print('Ket qua: Hop so')
                res = False

        else :
            print('Ket qua: Nguyen to')

        check.append(res)
    if all(check) :
        return f'{n} co the la nguyen to'
    else :
        return f'{n} la hop so'
n = int(input())
a,b = map(int, input().split())
    
print(Miler_Rabin(n,a,b))