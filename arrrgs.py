a, *b = 1, 2, 3


# Позиционные аргументы
# Ключевые аргументы
def example(a, b, *, c=5, d=4):
    print(a)
    print(b)
    print(c)
    print(d)


def my_print(*args, **kwargs):
    print(f'Got keywords: {kwargs}')
    for arg in args:
        print(str(arg))


if __name__ == '__main__':
    # example(1, 2)
    my_print(1, 2, 3, 4, 5, 6, sep=':', end='-')
