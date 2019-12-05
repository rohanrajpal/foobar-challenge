from pprint import pprint
import copy
from fractions import Fraction

def matmultiply(a,b):
	rowlen = len(a)
	collen = len(b[0])

	aux = [[ 0 for x in range(collen)]
				for y in range(rowlen)]

	for i in range(rowlen):
		for j in range(collen):
			for k in range(len(a[0])):
				aux[i][j] += (a[i][k] * b[k][j])

	return aux

def gcd(a,b):
	if b == 0:
		return a
	return gcd(b,a%b)

def lcm(arr):
	lcm = arr[0]
	for elem in arr[1:]:
		lcm = (lcm * elem / gcd(lcm,elem))
	return lcm

def transpose(m):
	return map(list,zip(*m))

def determinant(m):
	n = len(m)

	if n == 1:
		return m[0][0]

	if n == 2:
		return m[0][0]*m[1][1] - m[0][1]*m[1][0]

	total = 0
	for i in range(n):
		mAlt = copy.deepcopy(m)
		mAlt = mAlt[1:]
		colLen = len(mAlt)

		for j in range(colLen):
			mAlt[j] = mAlt[j][:i] + mAlt[j][i+1:]

		subdet = determinant(mAlt)
		total += ((-1) ** i) * m[0][i] * subdet

	return total

def minor(m,i,j):
	n = len(m)
	m = m[:i] + m[i+1:]
	for p in range(n-1):
		m[p] = m[p][:j] + m[p][j+1:]

	return m

def inverse(m):
	n = len(m)
	det = determinant(m)

	if n == 1:
		return [[m[0][0]/det]]
	if n == 2:
		return [ [m[1][1]/det, -1*m[0][1]/det],
				 [-1 * m[1][0]/det, m[0][0]/det ]]
	cofactors = [[0 for i in range(n)] for j in range(n)]
	
	for i in range(n):
		for j in range(n):
			cofactors[i][j] = ((-1)**(i+j)) * (determinant(minor(m,i,j))/det)

	return transpose(cofactors)

def convToProb(m):
	n = len(m)
	aux = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		if sum(m[i]) != 0:
			for j in range(n):
				aux[i][j] = m[i][j] / Fraction(sum(m[i]))
	return aux

def transform(m):
	n = len(m)
	t_states = []
	nt_states = []
	
	for i in range(n):
		if sum(m[i]) == 0:
			t_states.append(i)
		else:
			nt_states.append(i)
	
	label=[0 for i in range(n)]
	
	for i in range(len(nt_states)):
		label[nt_states[i]] = i
	for i in range(len(t_states)):
		label[t_states[i]] = i + len(nt_states)

	new_mat = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			new_mat[label[i]][label[j]] = m[i][j]

	return new_mat
def solution(m):
	nt_states = []
	n = len(m)
	m = transform(m)
	m = convToProb(m)

	if sum(m[0]) == 0:
		return [1,1]

	for i in range(n):
		if sum(m[i]) == 0:
			idiv = i
			break
	
	aux = m[:idiv]
	Q = []
	R = []
	for i in range(len(aux)):
		Q.append(aux[i][:idiv])
		R.append(aux[i][idiv:])
	
	for i in range(len(Q)):
		for j in range(len(Q)):
			if i==j:
				Q[i][j] = 1 - Q[i][j]
			else:
				Q[i][j] = - Q[i][j]

	fracs = matmultiply(inverse(Q), R) [0]

	numlist = []
	denomlist = []

	for x in fracs:
		numlist.append(x.numerator)
		denomlist.append(x.denominator)
	ans = []
	lcmdenom = lcm(denomlist)

	for i in range(len(numlist)):
		x = numlist[i]
		y = denomlist[i]
		ans.append(x * (lcmdenom / y))
	ans.append(lcmdenom)

	return ans


m1 = [[0,2,1,0,0],
      [0,0,0,3,4],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]
      ]
m2= 	[[0, 1, 0, 0, 0, 1],
		[0, 0, 0, 0, 0, 0],
		[4, 0, 0, 3, 2, 0],
		[0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0]]



m4 = 	[[0, 1, 0, 5, 0, 1],
		[0, 0, 1, 0, 0, 0], 
		[0, 0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 1], 
		[0, 0, 0, 0, 0, 0]]

m3 = [[0,0],[0,0]]
m5 =	[[0, 1, 0, 0, 0, 1],
		[4, 0, 0, 3, 2, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0]]

print(solution(m3))
# a = Fraction(3,10) * Fraction(5,9)
# print(Fraction(6,9))