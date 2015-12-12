# -*- coding: utf-8 -*-
res = []


def put(element):    # 'put'
    if element.isdigit():
        res.append(int(element))
    else:
        res.append(element)
    return res


def pop():
    res.pop()
    return res


def add():
    if type(res[-1]) == str:
        summ = ''
    else:
        summ = 0
    for i in range(-2, 0):
        summ += res[i]
        res.pop(i)
    res.append(summ)
    return res

def sub():


lines = (line.rstrip() for line in open('example.rtf'))

for line in lines:
    if line[:3] == 'put':
        put(line[4:])

    elif line == 'pop':
        pop()

    elif line == 'add':
        if type(res[-1]) == type(res[-2]):
            add()
        else:
            print 'Недопустимые типы данных'


print res

