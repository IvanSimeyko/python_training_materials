# -*- coding: utf-8 -*-

def message_level(file):
    """
    Подсчет и вывод суммарных сообщений разных уровней
    """
    critical = 0
    error = 0
    warning = 0
    info = 0
    debug = 0

    lines = (line.rstrip() for line in open(file))
    for i in lines:
        if i[0] == 'C':
            critical += 1
        elif i[0] == 'E':
            error += 1
        elif i[0] == 'W':
            warning += 1
        elif i[0] == 'I':
            info += 1
        elif i[0] == 'D':
            debug += 1
    return 'number critical = %d, error = %d, warning = %d, info = %d, debug = %d ' %\
           (critical, error, warning, info, debug)

#print message_level('logs/1.txt')


def list_component(file):
    """
    Вывод списка компонентов
    """
    d = {}
    res = []
    lines = (line.split('-') for line in open(file))
    for i in lines:
        if i[2] not in d:
            d[i[2]] = 1
        else:
            #print i[0]
            if i[0].rstrip() == "WARNING":
                d[i[2]] += 1
        num = d.values()
        for i in num:
            for key, values in d.iteritems():
                if i == values:
                    if key not in res:
                        res.append(key)
    return res


print list_component('logs/1.txt')



