
#讀取檔案
def read_file(file_name):
	conversation=[]
	with open(file_name,'r',encoding='utf-8-sig') as f:
		for line in f:
			conversation.append(line.strip())
	return conversation

#字行處理
def info(conversation):
	
	Allen_count=0
	Viki_count=0
	
	for line in conversation:
		s = line.split(' ')
		time = s[0]
		name = s[1]	

		if name == 'Allen':
			if s[2] == '貼圖' or s[2] == '圖片':
				continue
			else:
				for m in s[2:]:
					Allen_count += len(m)
	
		elif name == 'Viki':
			if s[2] == '貼圖' or s[2] =='圖片':
				continue
			else:	
				for m in s[2:]:
					Viki_count += len(m)

	print(Allen_count, Viki_count)
	return [Allen_count,Viki_count]
	
			

#回傳檔案
def save_file(a,b,file_name):
	with open(file_name,'w',encoding='utf-8-sig') as f:
		f.write(str(a)+','+str(b))

#主程式
def main(file_name,fn_output):
	conversation = read_file(file_name)
	X = info(conversation)
	save_file(X[0],X[1],fn_output)


x = input('please input file name you want to read')
y = input('please set the output file name')
main(x,y)

