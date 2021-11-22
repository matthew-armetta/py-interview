# Python interview questions

# add 2 numbers
def add_numbers(n1, n2):
    print(n1 + n2)


add_numbers(18, 20)


# reverse string (don't use reverse())
def reverse_string(s):
    r_string = ''
    for c in s:
        r_string = c + r_string

    print(r_string)


reverse_string('hello world')


# given 2 lists of unique numbers where 1 list contains all numbers from the other list minus 1, find the missing number
def find_missing(full, partial):
    mis_items = set(full) - set(partial)
    print(list(mis_items)[0])


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 5, 6, 7, 8, 9]
print(find_missing(list1, list2))


# find the average of a list of numbers
def get_average(numbers):
    total = 0
    for n in numbers:
        total += n
    print(total / len(numbers))


get_average([1, 4, 8, 2, 34, 34, 34, 7, 8, 9])
