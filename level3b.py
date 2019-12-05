
def solution(n):
	return len(divisions(n))

def divisions(n,visited = {}):
	if n == 0:
		return {}
	else:
		soln = {}
		for i in range(1,n+1):
			if i in visited:
				continue
			else:
				subsoln = divisions(i,visited union i)
				for x in subsoln:
					soln = soln union (i append subresult)
		return soln