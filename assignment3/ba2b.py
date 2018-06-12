
def distanceBetweenPatternsAndStrings(pattern, dna):
	k = len(pattern)
	distance = 0
	wordList = dna.split()
	for	text in wordList:
		hammingdistance = float('inf')
		for i in range(0, len(text)-k):
			if hammingdistance > hammingDistance(pattern, text[i:(i+k)]):
				hammingdistance = hammingDistance(pattern, text[i:(i+k)])

		distance += hammingdistance

	return distance

def hammingDistance(l1, l2):
	if(len(l1) != len(l2)):
		return 0
	else:
		return sum(i != j for i, j in zip(l1,l2))


def findMedianString(k, *args):
	distance = float('inf')
	median = ""
	for i in range(0, 4**k):
		pattern = numberToPattern(i, k)
		res = d(pattern, args)
		if res <= distance:
			distance = res
			median = pattern

	return median

def d (pattern, dna):
	total = 0
	for i in range(len(dna)):
		total += distanceBetweenPatternsAndStrings(pattern, dna[i])

	return total

def numberToPattern(index, k):
	if(k == 1):
		return (""+numberToSymbol(index))

	prefixIndex = index // 4
	r = index % 4
	prefixPattern = numberToPattern(prefixIndex, k-1)
	symbol = numberToSymbol(r)
	return prefixPattern + symbol


def numberToSymbol(num):
	if(num == 0):
		return 'A'
	elif(num == 1):
		return 'C'
	elif(num == 2):
		return 'G'
	elif(num == 3):
		return 'T'
	else:
		return '\0'

print("findMedianString: ")
print(findMedianString(3, "AAATTGACGCAT", "GACGACCACGTT", "CGTCAGCGCCTG",
					"GCTGAGCACCGG", "AGTACGGGACAG"))

