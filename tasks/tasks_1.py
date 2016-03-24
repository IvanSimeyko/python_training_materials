# -*- coding: utf-8 -*-


def decode(element):

    """
    Decodes a string (AON).
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
    #print temp

    #replace #
    for j in temp:
        if j != '#':
            res += j
        else:
            res += char
        char = j
    return res

print(decode('11122234###55'))


def gnome_sort(element):

    """
    Gnome sort
    Example [1, 2, 9, 0, 3, 4] => [0, 1, 2, 3, 4, 9]
    """

    i = 1
    while i < len(element):
        if element[i - 1] <= element[i]:
            i += 1
        else:
            tmp = element[i]
            element[i] = element[i - 1]
            element[i - 1] = tmp
            i -= 1
            if i == 0:
                i = 1
    return element

print(gnome_sort([1, 2, 9, 0, 3, 4]))