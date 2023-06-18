def  PrefixSum( BIT,  idx):
	sum = 0  #Iniialise sum 
	while (idx>0):
		sum += BIT[idx]
		idx -= idx & (-idx)
	return sum

def constructBIT(inp,n):
	BIT = [0]*(n+1)
	for i in range(1,n+1):
		BIT[i] = inp[i-1]

	for i in range(1,n+1):
		p = i + (i & -i)
		if p<=n: 
			BIT[p] = BIT[p] + BIT[i]

	return BIT


def update(BIT,idx,increment):
	while (idx < len(BIT)):
		BIT[idx] += increment
		idx += idx & -idx
