# -*- coding: utf-8 -*-


def decode(element):
    """Decodes a string (AON).
    Example: 11122234###55' => 1225
    """
    #remove duplicates
    temp = ''
    res = ''
    char = ''
    for i in element:
        if char == i and (len(temp) == 0 or temp[-1] != i):
            temp += i
        char = i
    #print(temp)

    #replace #
    for sym in temp:
        if sym != '#':
            res += sym
        else:
            res += char
        char = sym
    return res

print(decode('11122234###55'))
