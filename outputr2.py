
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
	for a in conversation:
		x = a.split(' ')
		name=x[1]
		dialogue=x[2]
		new_con.append([name,dialogue])
	return new_con

#回傳檔案
def save_file(new_con,file_name):
	with open(file_name,'w',encoding='utf-8-sig') as f:
		for line in new_con:
			f.write(line[0]+':'+line[1]+'\n')

#主程式
def main(file_name,fn_output):
	conversation = read_file(file_name)
	new_con = info(conversation)
	save_file(new_con,fn_output)


x = input('please input file name you want to read')
y = input('please set the output file name')
main(x,y)

