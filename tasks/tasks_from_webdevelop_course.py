def is_even(number):
    """
    Cтворити функцію з назвою is_even, яка буде приймати число і повертати булевий результат (True/False).
    True – число парне, False – число не парне. Результат повернути за допомогою ключового слова "return".
    """
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(10))
print(is_even(21))

