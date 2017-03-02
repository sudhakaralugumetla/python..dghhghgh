#functionlist
list = [10,20,30,50,60]
list2 = [10,20,30,40]
def addlist(list):
	sum=0;
	for ss in list:
		sum = sum+ss
	return sum
print cmp(list,list2)

print (addlist(list))