#### Задание 7.1
def task_1():

    #Дана строка. В каждой новой строке выведите её
    #подстроки, согласно заданию:

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
def task_2():

    #Напишите программу, которая отсекает всю часть строки
    #после первого слова.

    str = "Once upon a time"
    print("\nСтрока: ", str)
    newStr = str.split()
    print("Первое слово: ", newStr[0], "\n")
    taskChoice()

#### Задание 7.3
def task_3():

    #Дана строка, состоящая из слов, разделенных пробелами.
    #Определите, сколько в ней слов. Используйте для решения
    #задачи метод count. Выведите длину данной строки.

    str = "In the hole in the ground there lived a hobbit"
    print("\nСтрока: ", str)
    strCount = str.count(' ') + 1
    print("Всего слов: ", strCount, "\n")
    taskChoice()

#### Задание 7.4
def task_4():

    #Ввести с клавиатуры символьную строку и определить,
    #сколько в ней слов. Словом считается последовательность
    #непробельных символов, отделенная с двух сторон
    #пробелами (или стоящая с краю строки). Слова могут быть
    #разделены несколькими пробелами, в начале и в конце
    #строки тоже могут быть пробелы.

    str = input("\nВведите символьную строку: ").split()
    print("Всего слов: ", len(str), "\n")
    taskChoice()

#### Задание 7.5
def task_5():

    #Ввести с клавиатуры символьную строку и найти самое
    #длинное слово и его длину. Словом считается
    #последовательности непробельных символов, отделенная с
    #двух сторон пробелами (или стоящая с краю строки). Слова
    #могут быть разделены несколькими пробелами, в начале и
    #в конце строки тоже могут быть пробелы.

    str = input("\nВведите символьную строку: ").split()
    print(max(str, key=len))
    taskChoice()

#### Задание 7.6
def task_6():

    #Дана строка, состоящая ровно из двух слов, разделенных
    #пробелом. Переставьте эти слова местами. Результат
    #запишите в строку и выведите получившуюся строку.
        #При решении этой задачи не стоит пользоваться
        #циклами и инструкцией if

    str = "Hello, world!"
    print("\nСтрока: ", str)
    firstStr = str[:str.find(" ")]
    secondStr = str[str.find(" "):]
    print("Переставленные слова: ", secondStr, firstStr, "\n")
    taskChoice()

#### Задание 7.7
def task_7():

    #Дана строка. Разрежьте ее на две равные части (если длина
    #строки — четная, а если длина строки нечетная, то длина
    #первой части должна быть на один символ больше).
    #Переставьте эти две части местами, результат запишите в
    #новую строку и выведите на экран.
        #При решении этой задачи не стоит пользоваться
        #инструкцией if

    str = "Hello"
    print("\nСтрока: ", str)
    print(str[(len(str) + 1) // 2:] + str[:(len(str) + 1) // 2], "\n")
    taskChoice()

#### Задание 7.8
def task_8():

    #Дана строка. Если в этой строке буква f встречается только
    #один раз, выведите её индекс. Если она встречается два и
    #более раз, выведите индекс её первого и последнего
    #появления. Если буква f в данной строке не встречается,
    #ничего не выводите.
        #При решении этой задачи не стоит использовать циклы.

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
def task_9():

    #Дана строка. Найдите в этой строке второе вхождение
    #буквы f, и выведите индекс этого вхождения. Если буква f в
    #данной строке встречается только один раз, выведите
    #число -1, а если не встречается ни разу, выведите число -2.

    str = input("\nВведите строку: ").lower()
    if str.count("f") == -1:
        print("-1", "\n")
    elif str.count("f") < 1:
        print("-2", "\n")
    else:
        print(str.find('f', str.find('f') + 1), "\n")
    taskChoice()

#### Задание 7.10
def task_10():

    #Дана строка, в которой буква h встречается минимум два
    #раза. Удалите из этой строки первое и последнее
    #вхождение буквы h, а также все символы, находящиеся между ними.

    str = input("\nВведите строку: ").lower()
    str = str[:str.find('h')] + str[str.rfind('h') + 1:]
    print("Очищенная строка: ", str, "\n")
    taskChoice()

#### Задание 7.11
def task_11():
    print("Go out from my swamp!")

#### Задание 7.12
def task_12():
    print("Go out from my swamp!")

#### Задание 7.13
def task_13():
    print("Go out from my swamp!")

#### Задание 7.14
def task_14():
    print("Go out from my swamp!")

#### Задание 7.15
def task_15():
    print("Go out from my swamp!")

#### Задание 7.16
def task_16():
    print("Go out from my swamp!")

#### Задание 7.17
def task_17():
    print("Go out from my swamp!")

#### Задание 7.18
def task_18():
    print("Go out from my swamp!")

#### Задание 7.19
def task_19():
    print("Go out from my swamp!")

#### Задание 7.20
def task_20():
    print("Go out from my swamp!")

#### Задание 7.21
def task_21():
    print("Go out from my swamp!")

#### Задание 7.22
def task_22():
    print("Go out from my swamp!")

#### Задание 7.23
def task_23():
    print("Go out from my swamp!")

#### Задание 7.24
def task_24():
    print("Go out from my swamp!")

#### Задание 7.25
def task_25():
    print("Go out from my swamp!")

#### Задание 7.26
def task_26():
    print("Go out from my swamp!")

#### Задание 7.27
def task_27():
    print("Go out from my swamp!")

#### Задание 7.28
def task_28():
    print("Go out from my swamp!")

#### Задание 7.29
def task_29():
    print("Go out from my swamp!")

#### Задание 7.30
def task_30():
    print("Go out from my swamp!")

#### Функция выбора задания
def taskChoice():
    str = ""
    try:
        taskNumber = int(input("Введите номер задания: "))
        if taskNumber == 1: task_1()
        elif taskNumber == 2: task_2()
        elif taskNumber == 3: task_3()
        elif taskNumber == 4: task_4()
        elif taskNumber == 5: task_5()
        elif taskNumber == 6: task_6()
        elif taskNumber == 7: task_7()
        elif taskNumber == 8: task_8()
        elif taskNumber == 9: task_9()
        elif taskNumber == 10: task_10()
        elif taskNumber == 11: task_11()
        elif taskNumber == 12: task_12()
        elif taskNumber == 13: task_13()
        elif taskNumber == 14: task_14()
        elif taskNumber == 15: task_15()
        elif taskNumber == 16: task_16()
        elif taskNumber == 17: task_17()
        elif taskNumber == 18: task_18()
        elif taskNumber == 19: task_19()
        elif taskNumber == 20: task_20()
        elif taskNumber == 21: task_21()
        elif taskNumber == 22: task_22()
        elif taskNumber == 23: task_23()
        elif taskNumber == 24: task_24()
        elif taskNumber == 25: task_25()
        elif taskNumber == 26: task_26()
        elif taskNumber == 27: task_27()
        elif taskNumber == 28: task_28()
        elif taskNumber == 29: task_29()
        elif taskNumber == 30: task_30()
        else:
            print("Такого задания нет. Попробуйте вновь")
            taskChoice()
    except ValueError:
        print("Введите число.")
taskChoice()
