
def range_set(upperbound = 3200, lowerbound = 2000):
    mylist = [*range(2000,3200,1)]
    return mylist

def check_range(input):
    return range_set().__contains__(input)

def range_div():
    newlist = []
    for i in range_set():
        if (i%7 == 0) and (i%5 != 0):
            newlist.append(i)
    print(newlist)
    return newlist
def list_div():
    list7 = [number for number in range(2000,3201)
             if number%7 == 0 and number%5 != 0]
    return list7
def check_div(input):
    return range_div().__contains__(input)

if __name__ == '__main__':
    range_div()