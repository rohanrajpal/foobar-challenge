class Node:
	def __init__(self,x,y,dist=0):
		self.x = x
		self.y = y
		self.dist = dist

def getcoord(num):
	return Node(num//8, num%8)

def solution(src, dest):
	src = getcoord(src)
	dest = getcoord(dest)
	q = [src]
	visited = [[False for i in range(8)] for j in range(8)]
	xranges = [1,1,2,2,-1,-1,-2,-2]
	yranges = [2,-2,-1,1,2,2,1,-1]
	while len(q) > 0:
		cur = q.pop(0)
		if cur.x == dest.x and cur.y == dest.y:
			return cur.dist
		elif not visited[cur.x][cur.y]:
			visited[cur.x][cur.y] = True
			for i in range(8):
				nextx = cur.x + xranges[i]
				nexty = cur.y + yranges[i]
				if( 0 <= nextx <=7 and 0 <= nexty <= 7 and visited[nextx][nexty] == False):
					q.append(Node(nextx,nexty,cur.dist+1))

print(solution(19,20))