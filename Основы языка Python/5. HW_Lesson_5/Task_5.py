# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить её на экран.

def summary():
    try:
        with open('test_5.txt', 'w+') as file_5:
            line = input('Введите цифры через пробел \n')
            file_5.writelines(line)
            my_file = line.split()

            print(sum(map(int, my_file)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()