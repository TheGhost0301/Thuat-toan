def find_(pat,text):
    Lst = dict()# dùng dict bởi vì các phần tử trong dict có thể đc gán giá trị chữ cái thay cho số thứ tu
    chars = ''.join(text)
    for char in chars:
        Lst[char] = pat.rfind(char)
    return Lst

def Boyer_Moore(pat,text):

    Lst = find_(pat,text)
    x = []
    m = len(pat)
    n = len(text)
    i = m - 1
    j = m - 1
    count = 0
    while i < n :
        count +=1
        a = '{}: {} va {}'.format(count,text[i],pat[j])
        x.append(a)
        
        if text[i] == pat[j] :
            if j == 0:
                return i,x,count
            else :
                i = i - 1
                j = j - 1
        else :
            i = i + m - min(j, 1+Lst[text[i]])
            j = m - 1  
   
    return -1,x,count

p =input()
t =input()

a,b,c = Boyer_Moore(p,t)

if a > 0 :
    print('Su xuat hien cua mau "{}" trong van ban "{}" co vi tri bat dau la {}'.format(p,t,a))
    print('So phep lap la {}:'.format(c))
else:
    print('Mau "{}" khong xuat hien trong van ban "{}"'.format(p,t))
    print('So phep lap la {}:'.format(c))

print('   T va P')
for i in b:
    print(i)

