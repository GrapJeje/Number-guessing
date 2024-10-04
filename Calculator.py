def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def devide(a, b):
    if b == 0:
        return "Error"
    return a / b

while True:
    user_input = input("Geef jouw som: \n")
    
    output = "Error"

    if "+" in user_input:
        numbers = user_input.split("+")
        num1 = int(numbers[0].strip())
        num2 = int(numbers[1].strip())
        output = sum(num1, num2)

    elif "-" in user_input:
        numbers = user_input.split("-")
        num1 = int(numbers[0].strip())
        num2 = int(numbers[1].strip())
        output = subtract(num1, num2)

    elif "*" in user_input:
        numbers = user_input.split("*")
        num1 = int(numbers[0].strip())
        num2 = int(numbers[1].strip())
        output = multiply(num1, num2)

    elif "/" in user_input:
        numbers = user_input.split("/")
        num1 = int(numbers[0].strip())
        num2 = int(numbers[1].strip())
        output = devide(num1, num2)

    else:
        pass

    print(output)
