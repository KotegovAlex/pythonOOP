# global и nonlocal тлько для изменения значений
# global создает переменную в глобальном scope даже изнутри функции, nonlocal так сделать не может
# nonlocal ищет перменную в функции, в которую вложен, до глобал

counter = 100


def increment():
    # global counter
    counter = 0

    def inner1():
        def inner():
            # global counter
            nonlocal counter
            counter = 1
            print(counter)
        inner()

    inner1()


if __name__ == '__main__':
    increment()
