# -*- coding: utf-8 -*-

data = result = []

while True:
    n = raw_input(u'введите значение: ')
    if n == 'end':
        break
    else:
        data.append([int(s) for s in n.split()])
    print data

for i in range(len(data)):
    for j in range(len(data[0])):
        print data[i][j]
