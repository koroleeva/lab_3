def task1():
    n = int(input("Введите количество слов"))
    wnew = ""
    for i in range(n):
        word = input("Введите слово")
        wnew = wnew + " " + word
    print(wnew)


def task2():
    wnew = ""
    word = (input("Введите слово"))
    while word != ("stop"):
        word = (input("Введите слово"))
        wnew = wnew + " " + word
    print(wnew)


def task3():
    word = (input('Введите слово'))
    wnew = list(word.lower())
    letter = "ф" in wnew

    if letter:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")


def task4():
    i = 0
    while i < 4:
        from random import randint
        n = (randint(1, 9))
        m = (randint(1, 9))
        print(n, "+", m, "=", end=' ')
        s = (input())
        if s != n + m:
            i += 1



task3()