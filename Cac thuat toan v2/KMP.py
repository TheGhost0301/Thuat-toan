def get_prefix_table(pat):
    prefix_set = set()
    n = len(pat)
    prefix_table = [0]*n
    delimeter = 1
    while(delimeter<n):
        prefix_set.add(pat[:delimeter])
        j = 1
        while(j<delimeter+1):
            if pat[j:delimeter+1] in prefix_set:
                prefix_table[delimeter] = delimeter - j + 1
                break
            j += 1
        delimeter += 1
    return prefix_table

def strstr(text, pat):
  
    text_len = len(text)
    pat_len = len(pat)
    if (pat_len > text_len) or (not text_len) or (not pat_len):
        return -1
    prefix_table = get_prefix_table(pat)
    m = i = 0
    count = 0
    lst = []
    while((i<pat_len) and (m<text_len)):
        count += 1
        a = '{}: {} va {}'.format(count,text[m],pat[i])
        lst.append(a)
        if text[m] == pat[i]:
            i += 1
            m += 1
        else:
            if i != 0:
                i = prefix_table[i-1]
            else:
                m += 1
    if i==pat_len and text[m-1] == pat[i-1]:
        return m - pat_len , lst, count
    else:
        return -1, lst , count

if __name__ == '__main__':
    pat = input()
    text = input()
    #pat = 'aba'
    #text = 'abcaabacabaca'
    print(get_prefix_table(pat))
    a,b,c = strstr(text, pat)
    if a > 1 :
        print('Su xuat hien cua mau "{}" trong van ban "{}" co vi tri bat dau la {}'.format(pat,text,a))
    else :
        print('Mau "{}" khong xuat hien trong van ban "{}"'.format(pat,text))
    print('So phep lap la {}:'.format(c))
    for i in b:
        print(i)