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

# Втроенные фундкции map, zip, filter принимают в качевте аргументом интерируемые объекты
# и возвращают итераторы (в третьей ветке)

#  Функция zip принимает одну или несколько последовательностей в качестве аргуметов и возвращает
# список кортежей, составленных их соответствующих элементов этих кортежей (во второй ветке) или
# итерируемый объект (в третьей ветке)
c = zip((1,2), (3,4))
print(next(c))   # (1, 3)