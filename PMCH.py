import math
rna="GAUAUUCGCACGUCGCUUAGCAGCACUGCACACGUUGUCGCGUUAUAGAAACGGUCGACGGUUGUCACAGAC"
def pmch(rs):
	p=0
	r=0
	for i in rs:
		if i =="A":
			p+=1
		if i =="C":
			r+=1
        print(math.factorial(p) * math.factorial(r)) #FACTORIAL IS IMPORTED FROM MATH
print(pmch(rna))