'''
ЗАДАНИЕ 4

Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран
отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов

Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное ДЗ.
'''

num = 1
while num <= 100:
    if num % 10 == 1 and num != 11:
        print(num, 'процент')
    elif num % 10 == 2 and num != 12:
        print(num, 'процентa')
    elif num % 10 == 3 and num != 13:
        print(num, 'процентa')
    elif num % 10 == 4 and num != 14:
        print(num, 'процентa')
    else:
        print(num, 'процентов')
    num += 1
