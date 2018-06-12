
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

print("distanceBetweenPatternsAndStrings: ")
print(distanceBetweenPatternsAndStrings("AAA", "TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT"))

