# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(*args):
    try:
        a = int(input("Введите Делимое "))
        b = int(input("Введите Делитель "))
        res = a / b
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return res
    if b != 0:
        return a / b
    else:
        print("Значение не может быть равно нулю")

print(f'Результат  {div()}')