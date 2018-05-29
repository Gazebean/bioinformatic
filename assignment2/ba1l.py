def symbol_to_number(symbol):
    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    elif symbol == 'T':
        return 3
    else:
        return " "

def pattern_to_number(pattern):
    if pattern == "":
        return 0

    zeichen = pattern[-1]
    prefix = pattern[:-1]
    return 4 * pattern_to_number(prefix) + symbol_to_number(zeichen)

pattern = "CTTCTCACGTACAACAAAATC"
print (pattern_to_number(pattern))