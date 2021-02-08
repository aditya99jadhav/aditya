counter={}
word="BOOKKEEPER"
for w in word:
	count=counter.get(w)
	if count==None:
		counter[w]=1
	else:
		counter[w]=count+1

print(counter)

for key in counter:
	if counter[key]>1:
		print(key,counter[key])


	



