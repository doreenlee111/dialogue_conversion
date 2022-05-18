
#讀取檔案
def read_file(file_name):
	conversation=[]
	with open(file_name,'r',encoding='utf-8-sig') as f:
		for line in f:
			conversation.append(line.strip())
	return(conversation)

#字行處理
def info(conversation):
	new_con=[]
	person = none
	for a in conversation:
		if 'Allen' == a:
			name = 'Allen'
			continue

		elif a =='Tom':
			name = 'Tom'
			continue
		if person:
		new_con.append(name+':'+a)
	return new_con

#回傳檔案
def save_file(new_con,file_name):
	with open(file_name,'w') as f:
		for a in new_con:
			f.write(a+'\n')

#主程式
def main(file_name,fn_output):
	conversation = read_file(file_name)
	new_con = info(conversation)
	save_file(new_con,fn_output)


x = input('please input file name you want to read')
y = input('please set the output file name')
main(x,y)

