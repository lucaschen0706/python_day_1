# 計算讀入檔案的平均長度

data = []
new = []

length = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		length += len(line)
		if len(line) < 100:
			new.append(line)
print('AvgLength:', length / len(data))
print('一共有', len(new), '筆留言長度小於100')

print(new[0])
print(new[1])