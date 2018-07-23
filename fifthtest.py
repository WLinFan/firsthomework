number = list(range(1,101))
sum = 0
for i in number:
	if i%2 != 0:
		sum = sum + i
	else:
		sum = sum - i 
print(sum)
