import pprint

squares = [e ** 2 for e in range(10) if e % 2 == 0]
text = 'hello world'
words = [word.capitalize() for word in text.split()]

ints = [-1, 2, 0, 3, -4]
positives = [e for e in ints if e > 0]

letters = [letter for word in text.split() for letter in word if letter <= 'l']

matrix = [list(range(x, x + 3)) for x in range(3)]

unique_letters = {letter for word in text.split() for letter in word if letter < 'o'}

alphabet = {index: letter for index, letter in enumerate('abcdefghijklmnop', 1)}

positives_gen = (e for e in ints if e > 0)

if __name__ == '__main__':

    # print(list(positives_gen))
    print(next(positives_gen))
    print(next(positives_gen))

    # pprint.pprint(matrix, indent=1, width=15)
