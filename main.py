# Задача №1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно
# последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:


# def read_last(lines, file):
#     with open(file, 'r', encoding='utf-8') as file:
#         text_list = file.read().splitlines()
#         read_lines = [i for i in text_list if text_list]
#         print(read_lines[lines])
#
#
# read_last(7, 'article.txt')


# Задача №2 Требуется реализовать функцию longest_words(file), которая записывает в файл result.txt слово,
# имеющее максимальную длину (или список слов, если таковых несколько).

def longest_words(file):
    with open('article.txt', 'r', encoding='utf-8') as article:
        text = article.read().split()
        max_length = len(max(text, key=len))
        read_words = [text for text in text if len(text) == max_length]
        # result = ""
        if len(read_words) == 1:
            result = read_words[0]
        else:
            result = read_words
    with open(file, 'w', encoding='utf=8') as res:
        res.write(result)


longest_words('result.txt')
