# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
# строке.

file = open('test_2.txt', 'r')
text = file.read()
print('Содержимое файла: ', text, sep='\n')
file = open('test_2.txt', 'r')
text = file.readlines()
print('Количество строк в файле - ', len(text))
file = open('test_2.txt', 'r')
text = file.readlines()
for i in range(len(text)):
    print('Количество символов ', i + 1, ' - ой строки ', len(text[i]))
file = open('test_2.txt', 'r')
text = file.read()
text = text.split()
print('Общее количество слов - ', len(text))
file.close()