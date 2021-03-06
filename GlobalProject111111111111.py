# глобальные переменные
# Задание 1: объявить переменную, котоая будет хранить 15 значений
values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

print('Меню:')
print('1. Вывести на экран все значения')
print('2. Добавить значение')
print('3. Удалить значение')
print('4. Найти значение')
print('5. Отсортировать значения')
print('6. Выйти')
print('Введите опцию:')
userChoice = int(input())   # переменная, которая хранит выбор пользователя

# Задание 2: в цикле while создать ограничения для ввода опций таким образом, чтобы
# программа принимала только значения, из меню (1-6), в остальных случаях выдавала ошибку.

# Задание 3: Реализовать опцию 1 и 2 из списка меню.
while userChoice != 6:
    # Вывод ошибки, если userChoice больше или меньше 1 или 6
    if userChoice < 1 or userChoice > 6:
        print('Ошибка!')

    print('Введите опцию:', userChoice)

    print('Меню:')
    print('1. Вывести на экран все значения')
    print('2. Добавить значение')
    print('3. Удалить значение')
    print('4. Найти значение')
    print('5. Отсортировать значения')
    print('6. Выйти')
    print('Введите опцию:')
    userChoice = int(input())

    # Реализуем функцию 1
    if userChoice == 1:
        for i in values:
            print(i)

    # Реализуем функцию 2
    if userChoice == 2:
        newValue = input('Введите новое значение: ')
        values.append(newValue)

    # Реализуем функцию 3
    elif userChoice == 3:
        if len(values) != 0:
            print('Введите число для удаления:')
            searchValue = input()
            counter = 0
            deleted = False
            for count in range(0, len(values)):
                if (values[count] == searchValue) & (count < len(values)):
                    deleted = True
                    while count + 1 < len(values):
                        values[count] = values[count + 1]
                        count = count + 1
            if deleted is True:
                del values[count]
            elif deleted is False:
                print('Значения нет в базе данных.')
        else:
            print('База пустая! Добавьте значения!')
    # Реализуем функцию 4
    if userChoice == 4:
        foundValue = input('Введите значение, которое надо найти: ')
        for i in range(len(values)):
            if foundValue == values[i]:
                print('Индекс значения "{0}": {1}'.format(foundValue, i))
                break
            elif i == len(values) - 1:
                print('Такого значения нет в базе')
            else:
                pass

    # Реализуем функцию 5, но не указываем ключа, т.к его нет. Сортировка будет проводится так, как предписано в python
    if userChoice == 5:
        list1 = []
        list2 = []
        for i in values:
            try:
                i = int(i)
                list1.append(i)
            except ValueError:
                list2.append(i)
        values = sorted(list1) + sorted(list2)
        values = list(map(str, values))
