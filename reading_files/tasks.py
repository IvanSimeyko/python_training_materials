
def read_files(file_name):
    """
    Функция, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово
    в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, выводит лексикографически
    первое
    """
    d = {}
    res = [0, 0]
    with open(file_name) as inf:
        for line in inf:
            line = line.strip().lower().split()
            for element in line:
                if element not in d:
                    d[element] = 1
                elif element in d:
                    d[element] += 1
        print(d)
        for key, value in d.items():
            if value > res[1]:
                res[0] = key
                res[1] = value
            elif value == res[1]:
                if key < res[0]:
                    res[0] = key
                    res[1] = value
    return '%s %d' % (res[0], res[1])

# print(read_files('dataset_3363_3.txt'))


def students(file_name):
    """
    Функция, которая считывает файл, в котором в строке указывается фамили студента и его успеваемость по математике,
    фиизике и русскому и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке,
    соответствующей этому абитуриенту.
    Также в конце, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку
    по всем абитуриентам:
    """
    i = 0
    mathematics, physics, russian = 0, 0, 0
    lines = (line.strip().split(';') for line in open(file_name))
    for line in lines:
        average = (float(line[1]) + float(line[2]) + float(line[3])) / 3
        mathematics += float(line[1])
        physics += float(line[2])
        russian += float(line[3])
        i += 1.0
        print(average)
    print('{} {} {}'.format(mathematics/i, physics/i, russian/i))

students('dataset_3363_4.txt')

