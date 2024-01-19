def input_age():
    age = int(input("Enter your age: "))
    return age

def age_until_ret(age):
    ret = 65 - age
    if age >= 18:
        print(f"You are eligible to vote and you have {ret} years until retirement")
        return ret, True
    else:
        print(f"You are not eligible to vote and you have {ret} years until retirement")
        return ret, False

def pre_ret(age):
    pre_ret_age = 60 - age
    pre_ret_percent = (.60 + (0.08*(age - 60)))*100
    if age < 60:
        print(f"Years until pre retirement is {pre_ret_age} years")
        return pre_ret_age, None
    elif 60 <= age <= 65:
        print(f"Years until pre retirement is {pre_ret_age} years and percentage until full retirement {pre_ret_percent}%")
        return pre_ret_age, pre_ret_percent
    else :
        print(f"Years until pre retirement is {pre_ret_age} years and percentage until full retirement 100%")
        return pre_ret_age, 100

def drinking_age(age):
    if age >= 18:
        print("You are eligible to drink")
        return True
    else:
        print("You are not eligible to drink")
        return False


if __name__ == '__main__':
    age_input = input_age()
    age_until_ret(age_input)
    pre_ret(age_input)
    drinking_age(age_input)



