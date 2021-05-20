import os

#讀取檔案
def read_file(filename):
	chat = []
	with open(filename, 'r',encoding = 'utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
	return chat

def convert(lines):

	Allen_wc = 0
	Allen_sc = 0
	Allen_pc = 0

	Viki_wc = 0
	Viki_sc = 0
	Viki_pc = 0

	person = None
	for line in lines:
		s = line.split(' ')
		Time = s[0]
		Name = s[1]
		Chat = []
		if Name == 'Allen':
			if s[2] == '貼圖':
				Allen_sc += 1
			elif s[2] == '圖片':
				Allen_pc += 1
			else:
				for c in s[2:]:
					Allen_wc += len(c)
		elif Name == 'Viki':
			if s[2] == '貼圖':
				Viki_sc += 1
			elif s[2] == '圖片':
				Viki_pc += 1
			else:
				for c in s[2:]:
					Viki_wc += len(c)

	print('Allen說了:', Allen_wc , '傳了', Allen_sc, '貼圖', '傳了', Allen_pc, '圖片')
	print('Viki說了:', Viki_wc, '傳了', Viki_sc, '貼圖', '傳了', Viki_pc, '圖片')


def write_file(filename,lines):
	with open(filename, 'w' ,encoding = 'utf-8') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	
	input_filename = 'LINE-Viki.txt'
	output_filename = 'output.txt'
	lines = read_file(input_filename)
	
	lines = convert(lines)
	#write_file(output_filename, lines)
	
main()