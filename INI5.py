f=open('INSERT DIRECTORY\rosalind_ini5.txt', "r")
list = [ ]
for line in f:
	list.append(line)
lp=list[1::2]
for it in lp:
	print (it)