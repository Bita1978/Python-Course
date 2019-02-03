
def is_int(num):
    return type(num) is int


def input_number():
    try:
        num = int(input("Enter a number\n"))
        return num
    except ValueError:
        print(f"Error.. varible is not an int")
        return input_number()


def division(num1, num2):
    while not (is_int(num1) and is_int(num2)):
        num1 = input_number()
        num2 = input_number()
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Cannot operate with 0")
        num1 = input_number()
        num2 = input_number()
        return division(num1, num2)


# result = division("f", 8)
# print(result)

def read(path):
    try:
        with open(path, mode="r") as file:
            print(file.read())
    except FileNotFoundError:
        with open(path, mode="w") as file:
            file.write("hi")


read("hi.txt")
