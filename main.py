def task1():
    n = int(input("Введите количество слов"))
    snew = ""
    for i in range(n):
        slovo = input("Введите слово")
        snew = snew + " " + slovo
    print(snew)


def task2():
    snew = ""
    slovo = (input("Введите слово"))
    while slovo != ("stop"):
        slovo = (input("Введите слово"))
        snew = snew + " " + slovo
    print(snew)


def task3():
    slovo = (input('Введите слово'))
    for i in slovo:
        if (i == "ф"):
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")


task3()