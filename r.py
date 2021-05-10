# 計算讀入檔案的平均長度

data = []
length = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		length += len(line)
print('AvgLength:', length / len(data))

