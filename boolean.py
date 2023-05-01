# True (1), False (0)
# Создаются один раз при старте интерпретатора

# answers = ['Negative', 'Positive']
# x = 2
# print(answers[x >= 0])

# print(bool(1))
# print(bool('sfddsaf'))
# print(bool([]))
# print(bool(None))

falsy = [None, False, 0, 0.0, [], {}, set(), tuple(), range(0), '']


# print(bool(falsy)) # True
#
# for e in falsy:
#     print(bool(e)) # False

# class Cat:
#     pass
#
# cat = Cat()
# print(bool(cat))

# x, y = 1, 1
# print(bool(x and y))


def is_even(x) -> bool:
    return x % 2 == 0


print(is_even(3))