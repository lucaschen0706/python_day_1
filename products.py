import os
product = []
if os.path.isfile('product.csv'):
	print('yeah! 找到檔案了')
	with open('product.csv', 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name , price = line.strip().split(',')
			product.append([name, price])
	print(product)
else:
	print('找不到檔案.....')


while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []
	p.append(name)
	p.append(price)
	product.append(p)
print(product)

with open('product.csv', 'w') as f:
	f.write('商品,價格\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n')