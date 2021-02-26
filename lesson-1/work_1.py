''' ЗАДАНИЕ 1
Человеко-ориентированное представление интервала времени
Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:
1) до минуты: <s> сек;
2) до часа: <m> мин <s> сек;
3) до суток: <h> час <m> мин <s> сек;
4) сутки или больше: <d> дн <h> час <m> мин <s> сек
Например, если пользователь введет 4567 секунд, вывести:
1 час 16 мин 7 сек
'''

time = int(input('Введите количество секунд: '))
hour = time // 3600
minute = (time - (hour * 3600)) // 60
sec = (time - (hour * 3600) - (minute * 60)) // 1
print(hour, 'часов', minute, 'минут', sec, 'секунд')