def input_n():
    n = int(input("Enter your number: "))
    return n

def square_dict(n):
    square_dict = {i: i**2 for i in range(1, n + 1)}
    return square_dict

print(square_dict(3))