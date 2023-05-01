class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age

    def describe(self):
        print(f'I am {self.first_name} {self.last_name}, I am {self.__age} years old')

if __name__ == '__main__':
    ivan = Person('Ivan', 'Petrov', '20')
    ivan.describe()
