# Тело функцции выполняется всякий раз, когда происходит вызов функции:


def summ (a, b):

    """
    return sum of two elements
    """
    return a + b

x = summ(4, 5)    # вызов функции, тут выполнется тело функции
print(x)

help(summ)    # читаем строку документации
print(summ.__doc__)    # еще раз


# Обсласть видимости - место где опреляется переменна и выполняется ее поиск

x = 5    # глобальная переменная


def change_x(x):     # глобальная переменная
    x += 6     # локальная переменная
    return x

y = change_x(x)

print(x, y)    # значение х не поменялось

# Еще один интересный пример
GLOBAL_VAR = 10

def add_global_var(a):
    res = a + GLOBAL_VAR    # в области видимости функции переменная GLOBAL_VAR
    GLOBAL_VAR = 3          # задана после присваивания
    return res
# print(add_global_var(3))    # получим UnboundLocalError: local variable 'c' referenced before assignment

# Еще один пример, который пока не понятно как работает
def f3(v1, v2=[]):
    print(v2)
    v2.append(v1)
    return v2

#f3(0)    # [0]
#f3(1)    # [0,1]


# Переменные бывают локальные, нелокальные, глобальные, встроенные

# Замыкание - объект функции, который сохранияет значение в объемлющих областях видимости,
# даже  когда  эти  области могут  прекратить  свое существование.


def maker(n):
    def action(x):
        return x**n
    return action

f = maker(2)    # замыкание значения 2 в переменной  n

print(f(3))    # 9
print(f(4))    # 16

#Выражение lambda - выражение, которое генерирует функцию и сопровождается появлением новой локальной области видимости.


def func():
    x = 4
    action = (lambda n: n**4)
    return action

x = func()
print(x(2))    # 16


#Когда в аргументах передаются изменяемые объекты (списки, словари), непосредсвтенные изменения в таких
# объектах никуда не исчезнут после завершения функции и тем самым могут оказвать влияние на вызывающую программу.
# Передача в аргументах неизменяемых объектов (числа, строки, кортежи) напоминает копирование, поэтому изменение
# значений этих аругементов не приводит к  их изменению в вызывающей  программе.

def changer(a, b):    # В аргументах передаются ссылки на объекты
    a = 3             # Изменяется только значение локального имени
    b[0] = 'hello'    # Изменяется непосредсвтенно объект

x = 1
l = [1, 2]

changer(x, l)
print(x, l)    # (1, ['hello', 2,])

# Чтобы избежать изменений объектов, можно просто явно копировать изменяемые объекты

l = [1, 2]
changer(x, l[:])    # Передается копия поэтому переменная l не изменится
print(x, l)