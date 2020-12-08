# Создать текстовый файл (не программно).


my_file = open('test_2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('test_2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле (всего): - {len(content)} штук.')
my_file = open('test_2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов: {i + 1} - i line {len(content[i])} символ(а,ов).')
my_file = open('test_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Количество слов (всего): - {len(content)} слов.')
my_file.close()
