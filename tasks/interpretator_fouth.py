# -*- coding: utf-8 -*-

'''
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
    print(res[-1])


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
'''

class Fouth():

    """
    A simple interpreter language forth
    """
    res = []

    def __init__(self, name_file):
        self.file = name_file

    def put(self, element):
        if element.isdigit():
            self.res.append(int(element))
        else:
            self.res.append(element)
        return self.res

    def pop(self):
        self.res.pop()
        return self.res

    def add(self):
        if type(self.res[-1]) == str:
            j = ''
        else:
            j = 0
        for i in range(-2, 0):
            j += self.res[i]
            self.res.pop(i)
        self.res.append(j)
        return self.res


    def eval_forth(self):
        lines = (line.rstrip() for line in open(self.file))
        for line in lines:
            if line[:3] == 'put':
                self.put(line[4:])
            elif line == 'pop':
                self.pop()

            elif line == 'add':
                if type(self.res[-1]) == type(self.res[-2]):
                    self.add()
                else:
                    print 'Недопустимые типы данных для сложения'

            elif line[0] == '#':
                print 'it is comment'


a = Fouth('example.rtf')
print a.file
a.eval_forth()
print 'res= ', a.res


