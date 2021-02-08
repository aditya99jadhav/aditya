s1="EduCatiON"   #string

lc,uc=0,0      #initializing to 0

for s in s1:			#for loop for checking lc and uc
	if 'a'<=s<='z':
		lc=lc+1
	elif 'A'<=s<='Z':
		uc=uc+1

print("lowercase count=",lc)
print("uppercase count=",uc)
print(s1.swapcase()) 		#using swapcase function
