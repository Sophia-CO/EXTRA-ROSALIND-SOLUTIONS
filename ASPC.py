import math
a=1740
s=685
def aspc(sa,pc):
	fact = math.factorial #FACTORIAL IS IMPORTED FROM MATH
	return fact(sa)/fact(pc)/fact(sa-pc)
sum = 0
for i in range(s,a+1):
	sum = (sum + aspc(a,i)) % 1000000
print(sum)