from math import factorial
def pper(n, k):
	return factorial(n)/factorial(n-k) % 1000000
print (pper(85,9))