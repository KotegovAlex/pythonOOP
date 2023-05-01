# Синглтон - паттерн, когда считается, что в проекте будет существовать только один экземпляр класса
# Singleton "одиночка" - шаблон предоставления глобального доступа к состоянию
# Одна точка доступа к ресурсам/ данным и для того, чтобы ресурсоемкие задачи выполнять один раз
# плюсы: Один раз выполняем тяжелые задачи, имеет 1 вход для всей системы
# минусы: общесистемная глобальная переменная

# Monostate - шаблон глобального состояния (много объектов одного состояния)
# Singleton - шаблон глобальной переменной (один объект на всю систему)
# каждый модуль в пайтон это синглтон

class Singleton:
    instance = None

    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls)
            Singleton._do_work(Singleton.instance)
        return Singleton.instance

    def _do_work(self):
        print('do some hard work')
        # parse, db, work with data/ resources etc.
        self.data = 101


class Monostate:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        if not self._shared_state:
            print('do some hard work')
            # parse, db, work with data/ resources etc.
            self.data = 101


if __name__ == '__main__':
    first = Monostate()
    second = Monostate()
    print(first)
    print(second)
    print(first.data)
    first.data = 102
    print(second.data)
