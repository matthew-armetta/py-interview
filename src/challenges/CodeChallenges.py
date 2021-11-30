# Python interview questions


import math


def add_numbers(n1, n2):
    """adds 2 numbers and returns the result. validates that only int parameters are passed"""
    if not isinstance(n1, int) or not isinstance(n2, int):
        print(f"must be two ints ({n1}, {n2})")
        return None

    return n1 + n2


add_numbers(18, 20)


# reverse string (don't use reverse())
def reverse_string(s):
    r_string = ''
    for c in s:
        r_string = c + r_string
    return r_string


print(reverse_string('hello world'))


# given 2 lists of unique numbers where 1 list contains all numbers from the other list minus 1, find the missing number
def find_missing(full, partial):
    mis_items = set(full) - set(partial)
    return list(mis_items)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 5, 6, 7, 8, 9]
list3 = [2, 3, 4, 5, 6, 7, 8]
print(find_missing(list1, list2))
print(find_missing(list1, list3))


# find the average of a list of numbers
def get_average(numbers):
    total = 0
    for n in numbers:
        total += n
    print(total / len(numbers))


get_average([1, 4, 8, 2, 34, 34, 34, 7, 8, 9])


# print the numbers in a list line-by-line in reverse order
def reverse_print(alist):
    pass


# print the 4th element of a list of an error msg if does not exist
def print_4th(alist):
    pass


# get sq rt of number using math module
def sq_rt_of(n1):
    print(math.sqrt(n1))


sq_rt_of(25)
