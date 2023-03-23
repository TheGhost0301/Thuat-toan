P = input()
T = input()
def string_match(string, sub_str): 
	count = 0
	for i in range(len(string)-len(sub_str)+1): 
		index = i 
		count +=1
		for j in range(len(sub_str)): 
			if string[index] == sub_str[j]: 
				index += 1
				count+=1 
			else: 
				break 
			if index-i == len(sub_str): 
				return i ,count-1
	return -1 ,count

check, count = string_match(T,P)

if (check>0):
	print('Su xuat hien cua mau "{}" trong van ban "{}" co vi tri bat dau la {}, so phep lap la {}'.format(P,T,check,count))
else:
	print('Mau "{}" khong xuat hien trong van ban "{}", so phep lap la {}'.format(P,T,count))




