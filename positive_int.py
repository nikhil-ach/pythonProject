
numbers = [1, -2, 3, 4, 5, 6,-7, 8, 9]
def remove_negative(number):
    newlist = []
    for i in numbers:
        if i >= 0:
            newlist.append(i)
    return newlist

print(remove_negative(numbers))
