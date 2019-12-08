data = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		if len(data) % 10000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

length = 0
for d in data:
	length += len(d)
print('平均留言長度為: ', length / len(data), '個字')

filter1 = []
for d in data:
	if len(d) < 100:
		filter1.append(d)
print('留言少於100個字的共有: ', len(filter1), '筆')
