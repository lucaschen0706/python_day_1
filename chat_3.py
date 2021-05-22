lines = []
split_line = []

new = []

with open('3.txt' , 'r' , encoding='UTF-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	
	time = ''
	name = ''
	msg = ''

	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]

	for l in s[1:]:
		msg += l
	new.append([time , name , msg])

print(new)
	