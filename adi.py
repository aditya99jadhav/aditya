#n=int(input("enter a number: "))    

sum=0
i=1
print("numbers divisible by",42,"are:")
while i<=42:
	if (42%i==0):
		print(i,end=' ')
		sum=sum+i
	i=i+1
print("\nSum of divisors is:",sum)

sum=0
i=1
print("numbers divisible by",147,"are:")
while i<=147:
	if (147%i==0):
		print(i,end=' ')
		sum=sum+i
	i=i+1
print("\nSum of divisors is:",sum)
