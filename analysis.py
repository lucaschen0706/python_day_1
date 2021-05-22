# 計算每個字的出現頻率


data = []
count = 0

wof = [{'name':'', 'times':0}]

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		# if count % 1000 == 0:
			# print(len(data))
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] +=1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word , wc[word])
print(len(wc))

while True:
	word = input('請問你想查甚麼字:')
	if word == 'q':
		break
	if word in wc:
		print(wc[word])
	else:
		print('這個字沒出現過哦!')