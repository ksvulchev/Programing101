#!/usr/bin/python
def zero_insert(n):
	n = list(map(int,str(n)))
	arr = [n[0]]
	for i in range(1, len(n)):
		if n[i] == n[i-1] or (n[i] + n[i-1]) % 10 == 0:
			arr.append(0)
		arr.append(n[i])
	new_num = "".join(str(v) for v in arr)
	return new_num


print (zero_insert(461255))

