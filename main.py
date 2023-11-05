from funcs import get_add, get_sub
from itertools import chain
from functools import reduce

print(get_add(1, 2))
print(get_sub(10, 1))

print(*(x for x in "Hello World!" if x.isupper()))

print(list(chain(*map(lambda x: [x, x], filter(lambda x: x % 2 == 0, range(10))))))

print([i**3 for i in range(11) if i % 2 == 0])


def sum_of_squares(lst):
    return sum(i ** 2 for i in lst if i > 0)


print(sum_of_squares([1, 2, 3, -4, -5]))


def str_with_vowels():
    return (i for i in 'Hello' if i in ['a', 'e', 'i', 'o', 'u'])


print(next(str_with_vowels()))
print(next(str_with_vowels()))
print(next(str_with_vowels()))


def permutation_generator(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            rest = lst[:i] + lst[i+1:]
            for permutation in permutation_generator(rest):
                yield [lst[i]] + permutation


for i in permutation_generator([1, 2, 3]):
    print(i)
