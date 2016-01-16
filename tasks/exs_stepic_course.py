# -*- coding: utf-8 -*-
import math


def circle_len():

    """
    программа, которая подключает модуль math и, используя значение числа π
    из этого модуля, находит для переданного ей на стандартный ввод радиуса круга
    периметр этого круга и выводит его на стандартный вывод.
    """
    radius = int(input('введите радиус: '))
    length = math.pi * radius * 2
    return length


def football_result():
    """
    Функция, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на
    стандартный вывод сводную таблицу результатов всех матчей. Формат ввода следующий:
    В первой строке указано целое число n — количество завершенных игр.
    После этого идет n строк, в которых записаны результаты игры в следующем формате:
    Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
    Вывод программы необходимо оформить следующим образом:
    Команда:Всего_игр Побед Ничьих Поражений Всего_очков
    """
    n = 0
    result_all_games = []
    ans = {}
    result_function = ''
    games = int(input('Введите количество игр:'))
    while n < games:
        res_game = input('Введите результат игры: ').split(';')
        result_all_games.append(res_game)
        n += 1
    #print(result_all_games)
    for i in result_all_games:
        # добавляем название команды если ее нет
        if i[0] not in ans:
            ans[i[0]] = [0, 0, 0, 0, 0]
        if i[2] not in ans:
            ans[i[2]] = [0, 0, 0, 0, 0]
        # добавляем по одной игре в столбец сыгранных игр
        ans[i[0]][0] += 1
        ans[i[2]][0] += 1
        # заполняем оставшуюся часть таблицы
        if int(i[1]) < int(i[3]):
            ans[i[0]][3] += 1
            ans[i[2]][1] += 1
            ans[i[2]][4] += 3
        elif int(i[1]) == int(i[3]):
            ans[i[0]][2] += 1
            ans[i[0]][4] += 1
            ans[i[2]][2] += 1
            ans[i[2]][4] += 1
        elif int(i[1]) > int(i[3]):
            ans[i[2]][3] += 1
            ans[i[0]][1] += 1
            ans[i[0]][4] += 3
    # формируем требуемый вывод для функции
    for key, value in ans.items():
        result_function += key + ':'
        for elem in value:
            result_function += str(elem) + ' '
        result_function += '\n'
    return result_function

#print(football_result())


def substitution_cipher():
    """
    Функция принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита,
    на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом,
    и ещё одна строка, которую нужно расшифровать.
    """
    source = input('Введите исходный текст: ')
    cipher = input('Введите аналог зашифрованного текста: ')

    input_source = input("Введите строку, котоорую нужно зашифровать: ")
    input_cipher = input('Введите строку, которую нужно расшифровать: ')
    res_input = ''
    res_output = ''

    # первый вариант
    for i in input_source:
        if i in dict(zip(source, cipher)):
            res_input += dict(zip(source, cipher))[i]
    for i in input_cipher:
        if i in dict(zip(cipher, source)):
            res_output += dict(zip(cipher, source))[i]

    # второй вариант решения
    res_in = ''.join([dict(zip(source, cipher))[i] for i in input_source if i in dict(zip(source, cipher))])
    res_o = ''.join([dict(zip(cipher, source))[i] for i in input_cipher if i in dict(zip(cipher, source))])

    return res_input, res_in, res_output, res_o

#print(substitution_cipher())


def glossary():
    """
    Функция на стандартный ввод которой подаётся следующая структура: первой строкой — количество d записей в списке
    известных слов, после - d строк с одним словарным словом на строку, затем — количество l строк текста, после чего —
    l строк текста.
    Функция выводит выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается. Порядок
    вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе функции.
    """
    i = j = 0
    gloss = []
    text = []
    res = []
    answ = ''
    n = int(input('Количество записей в списке известных слов: '))
    while i < n:
        gloss.append((input('Введите одно слово для словаря: ')).lower())
        i += 1
    n = int(input('Введите колчичество строк текста: '))
    while j < n:
        text.append((input('Введите стрку текста: ')).lower().split())
        j += 1
    for i in text:
        for j in i:
            if j not in gloss:
                if j not in res:
                    res.append(j)
    for i in res:
        answ += i
        answ += '\n'
    return answ

print(glossary())