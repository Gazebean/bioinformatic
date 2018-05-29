def numbertosymbol(index):
    if index == 0:
        return "A"
    elif index == 1:
        return "C"
    elif index == 2:
        return "G"
    elif index == 3:
        return "T"
    else:
        return ' '

def numbertopattern(index,k):
    if k == 1:
        return numbertosymbol(index)
    return numbertopattern(index // 4, k-1) + numbertosymbol(index % 4)

index = 5353
k = 7
print(numbertopattern(index, k))