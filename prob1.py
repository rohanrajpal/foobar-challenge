import math
def solution(area):
	ansarr = []
	while(area != 0):
		num = findmaxsquare(area)
		ansarr.append(num)
		area = area - num
	return ansarr

def findmaxsquare(x):
	sq = int(math.sqrt(x)) 
	return sq*sq

print(solution(15324))