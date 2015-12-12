# -*- coding: utf-8 -*-
res = []


def put(element):
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
        j = ''
    else:
        j = 0
    for i in range(-2, 0):
        j += res[i]
        res.pop(i)
    res.append(j)
    return res


def sub():
    j = res[-2] - res[-1]
    for i in range(-2, 0):
        res.pop(i)
    res.append(j)
    return res


def random():
    print res[-1]


def eval_forth(file_name):
    """
    A simple interpreter language forth
    """
    lines = (line.rstrip() for line in open(file_name))

    for line in lines:
        if line[:3] == 'put':
            put(line[4:])

        elif line == 'pop':
            pop()

        elif line == 'add':
            if type(res[-1]) == type(res[-2]):
                add()
            else:
                print 'Недопустимые типы данных для сложения'

        elif line == 'sub':
            if type(res[-1]) == type(res[-2]) == int:
                sub()
            else:
                print 'Недопустимые типы данных для вычитания'

        elif line == 'print':
            random()

        elif line[0] == '#':
            print 'it is comment'

eval_forth('example.rtf')