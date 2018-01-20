class node:
	def __init__(self, x, y, z, n, m):
		self.x = x
		self.y = y
		self.z = z
		self.n = n
		self.m = m
		self.pos = [x,y,z,n,m]
	def setClust(self, c):
		self.cluster = c

'''讀檔'''
file = open('ecoli_test.txt',encoding='UTF-8').readlines()
lines = list()
for line in file:
	lines.append(line)
# print(lines[6])

'''整理好資料'''
attributes = list()
for i in range(len(lines)):
	line = (lines[i].split(','))
	del line[0], line[2], line[2], line[-1]     #刪第一行後index會隨著改變
	attributes.append(line)
# print(len(attributes))
# print(attributes[0][1])
'''刪除屬性的，已改到11行
# alist = []
# for i in range(len(attributes)):
# 	for j in range(8):
# 		if j==0 or j==3 or j==4:
# 			continue
# 		alist.append(attributes[i][j])
# print(alist)'''
	
'''設置個點座標與編號'''
nodes = []
for i in range(len(attributes)):
	x = float(attributes[i][0])
	# print(x)
	y = float(attributes[i][1])
	z = float(attributes[i][2])
	n = float(attributes[i][3]) 
	m = float(attributes[i][4]) 
	tmp = node(x, y, z, n, m)
	tmp.setClust(i)
	nodes.append(tmp)
# for nd in nodes:
# 	print(nd.pos)         #nodes存放很多物件(node)的list

vector = []
for i in range(len(nodes)):
	vector.append(nodes[i])
# print(vector[0].m)     #可以印出各點各座標值
	
minDist = float('inf')           #無限大意思，也可以隨便設一個很大的數
minI = 0
minJ = 0
for i in range(len(vector)):
	for j in range(len(vector)):
		if i != j:                 #leave one out方法，自己不算和其餘點算距離
			tmpDist = 0
			tmpDist += (vector[i].x - vector[j].x)**2
			tmpDist += (vector[i].y - vector[j].y)**2
			tmpDist += (vector[i].z - vector[j].z)**2
			tmpDist += (vector[i].n - vector[j].n)**2
			tmpDist += (vector[i].m - vector[j].m)**2
			tmpDist **= 0.5                             #L2 norm方法，兩點各座標值相減平方，再相加，再開根號
			if tmpDist < minDist:
				minDist = tmpDist
				minI = i
				minJ = j
a = vector[minI]
b = vector[minJ]           #先找到最近的兩個點a和b
# print(a.pos)
# print(b.pos)
for i in range(len(nodes)):
	if nodes[i].cluster = b.cluster:
		nodes[i].setClust(a.cluster)

