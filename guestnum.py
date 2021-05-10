import random

start = int(input('請決定隨機數字範圍開始值: '))
end = int(input('請決定隨機數字範圍結束值: '))
num = random.randint(start, end)
count = 0

while True:
	count += 1
	guest = int(input('猜猜看數字是多少: '))
	if guest > num:
		print('比答案大')
	elif num > guest:
		print('比答案小')
	else:
		print('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	print('這是你猜的第', count, '次')