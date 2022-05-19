s=[]
with open('3.txt','r',encoding='utf-8-sig') as f:
	for line in f:
		s.append(line.strip())

for line in s:
	s1 = line.split(' ')
	time=s1[0][:5]
	name=s1[0][5:]
	
	print(name)