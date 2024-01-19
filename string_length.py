def stringLength(my_list):

    count = 0
    if len(my_list)>=2:
        for word in my_list:
            if word[0] == word[-1]:
                count += 1
    else:
        count = 0

    return count