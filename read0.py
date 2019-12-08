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

filter1 = [] # 留言少於100個字的清單
for d in data:
	if len(d) < 100:
		filter1.append(d)
print('留言少於100個字的共有: ', len(filter1), '筆')

filter2 = [] # say good reviews
for d in data:
	if 'good' in d:
		filter2.append(d)
print('說讚的留言筆數共有: ', len(filter2), '筆')
print('列舉說讚的第一筆內容: ')
print(filter2[0])
print('列舉說讚的第二筆內容: ')
print(filter2[1])
