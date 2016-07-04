def main():
	n=input("enter no:")
	inp=[]
	out=[]
	for i in range(n):
		a=input("")
		inp.append(a)
	inp.sort()
	print inp
	for i in range(n):
	 if inp[i] == i:

		 out.append(i)
	print out	

	
main()