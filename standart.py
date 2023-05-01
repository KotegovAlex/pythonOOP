# all() - все элементы True
# any() - хотя бы один элемент True
# Работают быстро до первого выполнения условия
# filter(None, ...) вернет только элементы равные True

# a_list = [1, 0, True]
# a_list = [0, 0, 1, 0, True, 'sd']
a_list = ['aaa', 'bb', 'cc', 'd']


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat({self.name=}, {self.age=})'


if __name__ == '__main__':
    # if any(a_list):
    #     print(list(filter(None, a_list)))
    #     print([e for e in a_list if e])
    # print(all(a_list))
    # print(any(a_list))
    # print(max(a_list))
    cats = [Cat('Tom', 3), Cat('Angela', 4), Cat('Bob', 5)]
    # print(max(cats, key=lambda cat: cat.name))
    # for cat in iter(cats):
    #     print(cat)
    #
    # for line in iter(input, 'end'):
    #     print(line.upper())

    ints = [int(e) for e in iter(input, '')]
    print(ints)
