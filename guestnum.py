import random

num = random.randint(1, 100)
while True:
	guest = int(input('猜猜看數字是多少: '))
	if guest > num:
		print('比答案大')
	elif num > guest:
		print('比答案小')
	else:
		print('終於猜對了!')
		break