# Контрольная работа №1. Выполнил Трошин А.В.
# Задание 1
def task_1():

    #Электронные часы показывают время в формате h:mm:ss,
    #то есть сначала записывается количество часов в диапазоне от 0 до 23,
    #потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд.
    #Количество минут и секунд при необходимости дополняются до двузначного числа нулями.
    #Программа получает на вход число n - количество секунд, которое прошло с начала суток.
    #Выведите показания часов, соблюдая формат.

    time = int(input("\nКол-во секунд, которое прошло с начала суток: "))

    hours = time // 3600
    minutes = (time % 3600) // 60
    seconds = (time % 3600) % 60
    tmp = hours / 24

    if tmp == int(tmp) and tmp > 0: hours = 0
    elif hours > 24: hours = hours - 24 * (hours // 24)
    if hours < 10: hours = "0" + str(hours)
    if minutes < 10: minutes = "0" + str(minutes)
    if seconds < 10: seconds = "0" + str(seconds)
    print("Показания часов: ", hours, ":", minutes, ":", seconds, "\n",sep="")
    taskChoice()
# Задание 2
def task_2():

    taskNum = int(input("\nВведите номер под-задания: "))
    if taskNum == 1:

        #Петя записался в кружок по программированию. На первом занятии Пете задали
        #написать простую программу. Программа должна делать следующее:
        #в заданной строке, которая состоит из прописных и строчных
        #латинских букв, она: удаляет все гласные буквы,
        #перед каждой согласной буквой ставит символ ".",
        #все прописные согласные буквы заменяет на строчные.
        #Гласными буквами считаются буквы "A", "O", "Y", "E", "U", "I",
        #а согласными — все остальные. На вход программе подается ровно одна строка,
        #она должна вернуть результат в виде одной строки, получившейся после обработки.

        str = input("\nВведите строку: ")
        for ch in str:
            if ch not in {'A', 'O', 'Y', 'E', 'U', 'I', 'a', 'o', 'y', 'e', 'u', 'i'}:
                print('.', ch, "\n", end='', sep='')
    if taskNum == 2:

        #Дано три числа. Упорядочите их в порядке не убывания

        firstNum = int(input("\nВведите первое число: "))
        secNum = int(input("Введите второе число: "))
        thirdNum = int(input("Введите третье число: "))
        if (firstNum > secNum): firstNum, secNum = secNum, firstNum
        if (secNum > thirdNum): secNum, thirdNum = thirdNum, secNum
        if (firstNum > secNum): firstNum, secNum = secNum, firstNum
        print("\nЧисла в порядке не убывания: ", firstNum, secNum, thirdNum, "\n")
    taskChoice()
# Задание 3
def task_3():

    #Улитка ползет по вертикальному шесту высотой H метров,
    #поднимаясь за день на A метров, а за ночь спускаясь на B метров.
    #На какой день улитка доползет до вершины шеста?

    H = int(input("\nВысота шеста (H): "))
    A = int(input("Поднимается на (A): "))
    B = int(input("Спускается за ночь (B): "))
    days = (H - 2 * B + A - 1) / (A - B);
    print("\nУлитра доползет до вершины за", days, "дней. \n")
    taskChoice()
#### Функция выбора задания
def taskChoice():
    try:
        taskNumber = int(input("Введите номер задания: "))
        if taskNumber == 1: task_1()
        elif taskNumber == 2: task_2()
        elif taskNumber == 3: task_3()
        else:
            print("\nТакого задания нет. Попробуйте вновь\n")
            taskChoice()
    except ValueError:
        print("\nВведите число.\n")
        taskChoice()
    except KeyboardInterrupt:
        print(" ")

print("\nДля выхода нажмите 'ctrl + c'\n")
taskChoice()
