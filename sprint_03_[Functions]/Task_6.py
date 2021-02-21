"""Generator function randomWord has as an argument list of words. It should return any random word from this list. Each time words are different until the end of the list is reached. Then words are taken from the initial list again.


For example if

list = ['book', 'apple', 'word']

books = randomWord(list)

then possible output example

first call of next(books) returns apple

second call of next(books) returns book

third call of next(books) returns word

fourth call of next(books) returns book"""


def randomWord(books):
    import random

    inner_list = books.copy()

    if len(books) == 0:
        yield None

    while True:

        book = inner_list.pop()

        if len(inner_list) == 0:
            inner_list = books.copy()
            random.shuffle(inner_list)

        yield book