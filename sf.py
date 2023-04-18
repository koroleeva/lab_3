# from random import randint
# n = 0
# q = 0
# while True:
#     a = randint(1, 20)
#     b = randint(1, 20)
#     print(f"{a} + {b} = ", end="")
#     res = input()
#
#     while not res.isdigit() and res != "stop":
#         print("попробуйте ввести число :)", end="")
#         res = input()
#     if res == "stop":
#         break
#     res = int(res)
#     if a + b == res:
#         print("Правильный ответ!")
#         q = q + 1
#     else:
#         print("Ответ неправильный!")
#         n = n + 1
#     if n == 3:
#         print(f"Вы проиграли. Количество правильных ответов:{q}")
#         break

from random import randint
mist=0
right=0
while mist!=3:
    m = randint(1, 10)
    n = randint(1, 10)
    summ=m+n
    print(m,"+",n)
    f=int(input())
    if f == summ:
        print("Правильно!")
        right+=1
    else:
        mist+=1
        print("Ответ неверный")
print("Игра окончена.", "Правильных ответов:", right)