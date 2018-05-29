def patterntonumber(pattern):
    if pattern == "":
        return 0
    symbol = pattern[-1]
    prefix = pattern [:-1]
    return 4 * patterntonumber(prefix) + symboltonumber(symbol)

def symboltonumber(symbol):
    if symbol == 'A':
        return 0
    if symbol == 'C':
        return 1
    if symbol == 'G':
        return 2
    if symbol == 'T':
        return 3

test = "ACGCGGCTCTGAAA"
k = 2

patternfrequencies =[0] * 4 ** k

for i in range(len(test)-k+1):
    pattern = test[i:i+k]
    x = patterntonumber(pattern)
    patternfrequencies[x] = patternfrequencies [x] + 1

z = ""
for i in patternfrequencies:
    z += str(i) + " "

print (z)