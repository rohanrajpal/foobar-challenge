memo = {}
# import sys
# sys.setrecursionlimit(1029)
def solution(n):
	return reduce(int(n))

def reduceold(n,acc=0):
	while True:
		if n == 1:
			return acc
		elif n % 2 == 1:
			(n,acc) = min((n-1,acc+1),(n+1,acc+1))
			continue
		else:
			(n,acc) = (n>>1,acc+1)
			continue
		break


def reducememo(n,acc=0):
	if n == 1:
		return 0
	elif memo.get(n,-1) != -1:
		return memo[n]
	elif n % 2 == 1:
		memo[n] = min(reducememo(n-1,acc+1),reducememo(n+1,acc+1))
	else:
		memo[n] = reducememo(n>>1,acc+1)

	return memo[n]

def reduce(n):
	if n <= 1:
		return 0
	elif memo.get(n,-1) != -1:
		return memo[n]
	elif n%2 == 1:
		memo[n] = 2 + min(reduce((n-1)>>1), reduce((n+1)>>1))
	else:
		cnt=0
		alt = n
		while alt%2 == 0:
			cnt+=1
			alt = alt>>1
		memo[n] = cnt + reduce(alt)

	return memo[n]
def redsimple(n):
	if n<=1:
		return 0
	elif n%2 == 1:
		return 1+min(redsimple(n-1),redsimple(n+1))
	else:
		return 1+ redsimple(n>>1)

def iterative(n):
	stack = [n]
	memo[1] = 0
	while len(stack) > 0:
		cur = stack.pop()
		if cur > 1:	
			if cur%2 == 1:
				if memo.get(cur-1,-1) != -1 and memo.get(cur+1,-1) != -1:
					memo[cur] = min(1+ memo[cur-1],1+ memo[cur+1])
					continue
				
				stack.append(cur)
				stack.append(cur+1)
				stack.append(cur-1)
			else:
				if memo.get(cur>>1,-1) != -1:
					memo[cur] = 1 + memo[cur>>1]
					continue
				stack.append(cur)
				stack.append(cur>>1)

	return memo[n]
				
				


def redacc(n,acc=0):
	if n<=1:
		return acc
	elif n%2 == 1:
		(n,acc) = min(redacc(n-1,acc+1),redacc(n+1,acc+1))
	else:
		(n,acc) = redacc(n>>1,acc+1)

	return acc
string = ''
for i in range(309):
	string += '9'

# print(len(string))
print(iterative(int(15)))