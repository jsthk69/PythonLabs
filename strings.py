#### Функция выбора задания
def taskChoice():
    str = ""
    try:
        taskNumber = int(input("Введите номер задания: "))
        if 1 > taskNumber > 30:
            print("Такого задания нет. Попробуйте вновь")
            taskChoice()
        else:
            if taskNumber == 1: taskOne()
            if taskNumber == 2: taskTwo()
            if taskNumber == 3: taskThree()
            if taskNumber == 4: taskFour()
            if taskNumber == 5: taskFive()
            if taskNumber == 6: taskSix()
            if taskNumber == 7: taskSeven()
            if taskNumber == 8: taskEight()
            if taskNumber == 9: taskNine()
            if taskNumber == 10: taskTen()
            if taskNumber == 11: taskEleven()
            if taskNumber == 12: taskTwelve()
            if taskNumber == 13: taskThirteen()
            if taskNumber == 14: taskFourteen()
            if taskNumber == 15: taskFifteen()
            if taskNumber == 16: taskSixteen()
            if taskNumber == 17: taskSeventeen()
            if taskNumber == 18: taskEighteen()
            if taskNumber == 19: taskNineteen()
            if taskNumber == 20: taskTwenty()
            if taskNumber == 21: taskTwentyOne()
            if taskNumber == 22: taskTwentyTwo()
            if taskNumber == 23: taskTwentyThree()
            if taskNumber == 24: taskTwentyFour()
            if taskNumber == 25: taskTwentyFive()
            if taskNumber == 26: taskTwentySix()
            if taskNumber == 27: taskTwentySeven()
            if taskNumber == 28: taskTwentyEight()
            if taskNumber == 29: taskTwentyNine()
            if taskNumber == 30: taskThirty()
    except ValueError:
        print("Введите число.")

#### Задание 7.1
def taskOne():
    str = "Abrakadabra"
    print("\nСтрока: ", str)
    print("Третий символ строки: ", str[2])
    print("Предпоследний символ: ", str[-2])
    print("Первые 5 символов: ", str[0:5])
    print("Вся строка, кроме последний двух: ", str[0:-2])
    print("Символы с четным индексом: ", str[::2])
    print("Символы с нечетным индексом: ", str[1::2])
    print("Символы в обратном порядке: ", str[::-1])
    print("Символы через один, в обратном порядке: ",str[::-2])
    print("Длинна строки: ", len(str), "\n")
    taskChoice()
#### Задание 7.2
def taskTwo():
    str = "Once upon a time"
    print("\nСтрока: ", str)
    newStr = str.split()
    print("Первое слово: ", newStr[0], "\n")
    taskChoice()
#### Задание 7.3
def taskThree():
    str = "In the hole in the ground there lived a hobbit"
    print("\nСтрока: ", str)
    strCount = str.count(' ') + 1
    print("Всего слов: ", strCount, "\n")
    taskChoice()
#### Задание 7.4
def taskFour():
    str = input("\nВведите символьную строку: ").split()
    print("Всего слов: ", len(str), "\n")
    taskChoice()
#### Задание 7.5
def taskFive():
    str = input("\nВведите символьную строку: ").split()
    print(max(str, key=len))
    taskChoice()
#### Задание 7.6
def taskSix():
    str = "Hello, world!"
    print("\nСтрока: ", str)
    firstStr = str[:str.find(" ")]
    secondStr = str[str.find(" "):]
    print("Переставленные слова: ", secondStr, firstStr, "\n")
    taskChoice()
#### Задание 7.7
def taskSeven():
    str = "Hello"
    print("\nСтрока: ", str)
    print(str[(len(str) + 1) // 2:] + str[:(len(str) + 1) // 2], "\n")
    taskChoice()
#### Задание 7.8
def taskEight():
    str = input("\nВведите строку: ").lower()
    firstEntry = str.find('f')
    lastEntry = str.rfind('f')
    if firstEntry == -1:
        print("F отстутвует.", "\n")
    elif firstEntry == lastEntry:
        print(firstEntry, "\n")
    else:
        print(firstEntry, lastEntry, "\n")
    taskChoice()
#### Задание 7.9
def taskNine():
    str = input("\nВведите строку: ").lower()
    if str.count("f") == -1:
        print("-1", "\n")
    elif str.count("f") < 1:
        print("-2", "\n")
    else:
        print(str.find('f', str.find('f') + 1), "\n")
    taskChoice()
#### Задание 7.10
def taskTen():
    str = input("\nВведите строку: ").lower()
    str = str[:str.find('h')] + str[str.rfind('h') + 1:]
    print("Очищенная строка: ", str, "\n")
    taskChoice()
#### Задание 7.11
def taskEleven():
    print("Go out from my swamp!")
#### Задание 7.12
def taskTwelve():
    print("Go out from my swamp!")
#### Задание 7.13
def taskThirteen():
    print("Go out from my swamp!")
#### Задание 7.14
def taskFourteen():
    print("Go out from my swamp!")
#### Задание 7.15
def taskFifteen():
    print("Go out from my swamp!")
#### Задание 7.16
def taskSixteen():
    print("Go out from my swamp!")
#### Задание 7.17
def taskSeventeen():
    print("Go out from my swamp!")
#### Задание 7.18
def taskEighteen():
    print("Go out from my swamp!")
#### Задание 7.19
def taskNineteen():
    print("Go out from my swamp!")
#### Задание 7.20
def taskTwenty():
    print("Go out from my swamp!")
#### Задание 7.21
def taskTwentyOne():
    print("Go out from my swamp!")
#### Задание 7.22
def taskTwentyTwo():
    print("Go out from my swamp!")
#### Задание 7.23
def taskTwentyThree():
    print("Go out from my swamp!")
#### Задание 7.24
def taskTwentyFour():
    print("Go out from my swamp!")
#### Задание 7.25
def taskTwentyFive():
    print("Go out from my swamp!")
#### Задание 7.26
def taskTwentySix():
    print("Go out from my swamp!")
#### Задание 7.27
def taskTwentySeven():
    print("Go out from my swamp!")
#### Задание 7.28
def taskTwentyEight():
    print("Go out from my swamp!")
#### Задание 7.29
def taskTwentyNine():
    print("Go out from my swamp!")
#### Задание 7.30
def taskThirty():
    print("Go out from my swamp!")

#### Вызов стартовой функции выбора задания
taskChoice()
