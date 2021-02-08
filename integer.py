list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  #given list

print("")
  
print("given list: ",list1) 	#printing the list

print("")

print("elements and positions of elements that are divisble by 2 are as follows:")

print("")

for ele in list1: 
	if ele%2==0:		#numbers divisble by 2 
		print("position of",ele,"in the list is:",list1.index(ele))
