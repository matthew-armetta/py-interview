# Python interview questions


######################################################################################
# Reverse a String (don't use reverse())
######################################################################################
def reverse_string(s):
    r_string = ''
    for c in s:
        r_string = c + r_string

    return r_string


print(reverse_string('hello world'))
######################################################################################


######################################################################################
# Given 2 lists of unique numbers where 1 list contains all numbers from the other list minus 1, find the missing number
######################################################################################
def find_missing(full, partial):
    mis_items = set(full) - set(partial)
    return list(mis_items)[0]
    print(mis_items)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 5, 6, 7, 8, 9]
print(find_missing(list1, list2))
######################################################################################


######################################################################################

######################################################################################

