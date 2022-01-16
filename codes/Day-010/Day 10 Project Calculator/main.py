# Calculator
from art import logo
from clear_console import cls


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculator():
    cls()
    print(logo)

    should_continue = True
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while should_continue:
        operation_symbol = input("Pick an operations: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        tr = input(
            f"Type 'y' to continue calculation with {answer}, type 'n' to start a new calculation: or type 'e' to exit: ")

        if tr == 'y':
            num1 = answer
        elif tr == 'n':
            should_continue = False
            calculator()
        else:
            should_continue = False


calculator()
