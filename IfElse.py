coordinates = (4, 5)
print(coordinates[1])


def say_hi():
    print("Hello User")


say_hi()


def cube(num):
    return num*num*num


result = cube(4)
print(cube(3))
print(result)

is_male = True
is_tall = True

if is_male:
    print("You are a male")
else:
    print("you are not a male")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))


num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operation")



