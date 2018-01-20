# from operator import itemgetter
import os
import sys
import codecs   #編碼轉換用

class node:
	def __init__(self, x, y, z, n, m):
		self.x = x
		self.y = y
		self.z = z
		self.n = n
		self.m = m
		self.pos = [x,y,z,n,m]
	def setClass(self, c):
		self.myclass = c

'''讀檔'''
file = open('ecoli.txt',encoding='UTF-8').readlines()
lines = list()
for line in file:
	lines.append(line)
# print(lines[6])

'''整理好資料'''
attributes = list()
name = list()
for i in range(len(lines)):
	line = (lines[i].split(','))
	name.append(line[0])
	del line[0], line[2], line[2]     #刪第一行後index會隨著改變，也可以從後面減就不會影響index
	
	line[-1] = line[-1].replace("\n","")
	attributes.append(line)
	# print(line)
# print(len(attributes))
# print(attributes[0][0])
# print(name)

'''設置個點座標與類別'''
nodes = []
for i in range(len(attributes)):
	x = float(attributes[i][0])
	# print(x)
	y = float(attributes[i][1])
	z = float(attributes[i][2])
	n = float(attributes[i][3]) 
	m = float(attributes[i][4]) 
	tmp = node(x, y, z, n, m)
	if attributes[i][5]=='cp':
		tmp.setClass('cp')
	if attributes[i][5]=='im':
		tmp.setClass('im')
	if attributes[i][5]=='imS':
		tmp.setClass('imS')
	if attributes[i][5]=='imL':
		tmp.setClass('imL')
	if attributes[i][5]=='imU':
		tmp.setClass('imU')
	if attributes[i][5]=='om':
		tmp.setClass('om')
	if attributes[i][5]=='omL':
		tmp.setClass('omL')
	if attributes[i][5]=='pp':
		tmp.setClass('pp')
	nodes.append(tmp)
# print(nodes[1].myclass)

'''寫檔'''
dirName = 'practice1'
fileName = 'output'
if not os.path.exists(dirName):
	os.makedirs(dirName)
fileout = codecs.open('output.txt','w','utf-8')
fileout.write('Name\tForecast\tCategory')
fileout.write('\n')

'''創一個新物件，vector是指標(nodes也是指標)'''
vector = []
for i in range(len(nodes)):
	v = node(nodes[i].x,nodes[i].y,nodes[i].z,nodes[i].n,nodes[i].m)
	v.setClass(nodes[i].myclass)
	vector.append(v)
# print(vector[2].myclass)

minDist = []
minI = 0
minJ = []
f = []
ALL = []

for i in range(len(vector)):
	minJ = []
	for j in range(len(vector)):
		dictDist = {}              #!!每次迴圈重新宣告，不然會重複的值繼續做運算!!!
		if i != j:                 #leave one out方法，自己不算和其餘點算距離
			tmpDist = 0
			tmpDist += (vector[i].x - vector[j].x)**2
			tmpDist += (vector[i].y - vector[j].y)**2
			tmpDist += (vector[i].z - vector[j].z)**2
			tmpDist += (vector[i].n - vector[j].n)**2
			tmpDist += (vector[i].m - vector[j].m)**2
			tmpDist **= 0.5                             #L2 norm方法，兩點各座標值相減平方，再相加，再開根號
			dictDist['dist'] =  tmpDist                 #加入dictionary,key:j,value:tmpDist
			dictDist['index_i'] =  i
			dictDist['index_j'] =  j
			minI = i
			# print(i,j,tmpDist)
			minJ.append(dictDist)
			minJ.sort(key=lambda d:d['dist'])     #,reverse = True)
	# print(minJ)
	f = []
	for n in range(5):
		# print(minJ[n]['index_j'])
		f.append(minJ[n]['index_j'])
	print(f)                                #印出距離最小的五個點
	ALL.append(f)
	# print(ALL)
	# v = vote(f)
	dicCont = {}
	result = []
	for index in range(len(f)):
		# print(f[index])
		for j in range(len(vector)):
			if f[index] == j:
				result += [vector[j].myclass]
				dicCont[result[index]] = 0 
	print(result,"class")                   #找出五個點的對應類別
	
	conList = []
	rank = []
	for index in range(len(result)):
		# count = 0
		dicCont[result[index]]=0
		for j in range(len(result)):
			if result[index] == result[j]:
				dicCont[result[index]] = dicCont[result[index]]+1	
	print(dicCont)                                            #算出五個點中各類別出現幾次  
	rank = sorted(dicCont.items(),key=lambda d: d[1],reverse = True)                                          			
	print(rank)                                                #各類別出現幾次，排序後(大到小)
	
	if rank[0][1] == 5:                 #投票50時
		vector[i].setClass(rank[0][0])
	elif rank[0][1] > rank[1][1]:         #第一個數為最大時，沒有其他相同的count
		vector[i].setClass(rank[0][0])
	elif rank[0][1] == rank[1][1]:
		if rank[0][1]==1:               #投票1111時
			vector[i].setClass(nodes[ALL[len(ALL)-1][0]].myclass)
			print("11111")
			# for n in range(4):
			# 	print(minJ[n]['dist'],"+")
			# 	print(ALL[len(ALL)-1])
		elif rank[0][1]==2:               #投票221時
			vector[i].setClass(nodes[ALL[len(ALL)-1][0]].myclass)
			print("221")
			print(ALL[len(ALL)-1])            #第ALL[len(ALL)]的點，index要-1
	print ('i:', i)
	print('predict:', vector[i].myclass)
	print('actual:\t', nodes[i].myclass)		
	print("--")
	fileout.write(name[i]+'\t')
	fileout.write(vector[i].myclass+'\t')
	fileout.write(nodes[i].myclass+'\t')
	fileout.write("\n")

correct = 0
for i in range(len(vector)):
	if vector[i].myclass == nodes[i].myclass:
		print(i, vector[i].myclass,"預測",nodes[i].myclass,"實際","true")
		correct = correct+1
	if vector[i].myclass != nodes[i].myclass:
		print(i, vector[i].myclass,"預測",nodes[i].myclass,"實際","false")

accuracy = correct/len(nodes)
print('\n準確率:',accuracy)

fileout.write('\nCorrect Rate:')
fileout.write(str(accuracy))
fileout.close()



		# for m in range(len(vector))
		# v = vote()
		# vector[f].myclass = setClass(v)


# print(ALL)
# print(ALL[0][1])

# dicCont = {}
# result = []
# for i in range(len(f)):
# 	# print(f[i])
# 	for j in range(len(vector)):
# 		if f[i] == j:
# 			result += [vector[j].myclass]
# 			dicCont[result[i]] = 0 
# print(result,"class")

# conList = []
# rank = []
# for i in range(len(result)):
# 	# count = 0
# 	dicCont[result[i]]=0
# 	for j in range(len(result)):
# 		if result[i] == result[j]:
# 			dicCont[result[i]] = dicCont[result[i]]+1
			# count = count+1
		
	# conList.append(count)
# print(conList,"次數")
# print(dicCont)
# rank = sorted(dicCont.items(),key=lambda d: d[1],reverse = True)
# print(rank)
# print(rank[0][1])

# for i in range(len(rank)):
# 	for j in range(len(rank)):

# if rank[0][1] > rank[1][1]:
# 	setclass(rank[0][0])
# if rank[0][1] == rank[1][1]:
# 	if rank[0][1]==1:               #投票1111時


			# else:
			# 	minI = i
			# 	sort(minDist,reverse = True)            #第6個之後，先將list做大到小排列
			# 	if tmpDist < minDist[0]:    #and minDist[0] != minDist[n for n in range(5)]:                
			# 		minDist.pop([0])                    
			# 		minDist.append(tmpDist)
			# 	if tmpDist == minDist[0]:
			# 		minDist.append(tmpDist)


				