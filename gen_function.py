# Если есть yield - значит функция является генератором
# Генератор ленивый - работает только при переборе (next)


squares = (e ** 2 for e in range(0, 11, 2))


def squares2():
    for e in range(0, 11, 2):
        yield e ** 2


def pause():
    while True:
        print(a)
        yield a

a = 10
gen = pause()

# gen = squares2()
# print(gen)
#
# print(next(gen))
# print(next(gen))
# print(next(gen))


# for square in gen:
#     print(square)
