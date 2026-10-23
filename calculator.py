import math
from typing import Literal, TypeIs, get_args

Operator = Literal["+", "-","*", "/"]

def is_operator(text: str) -> TypeIs[Operator]:
    return text in get_args(Operator)

def add(a: float, b:float) -> float:
    return a + b

def subtract(a:float, b:float) -> float:
    return a - b

def multiply(a:float, b:float) -> float:
    return a * b

def divide(a:float, b:float) -> float:
    return a / b

def calculate(a:float, op:Operator, b:float) -> float:
    match op:
        case "+":
            return add(a,b)
        case "-":
            return subtract(a,b)
        case "*":
            return multiply(a,b)
        case "/":
            return divide(a,b)
        case _:
            raise ValueError(f"unknown operator {op!r}")


def parse_number(text: str) -> float:
    trimmed = text.strip()
    if trimmed == "":
        raise ValueError("please enter a number")
    try:
        value = float(trimmed)
    except ValueError:
        raise ValueError(f"{trimmed!r} is not a valid number") from None

    if not math.isfinite(value):
        raise ValueError(f"{trimmed!r} is not a valid number")
    return value



def ask_number(prompt: str) -> float:
    while True:
        answer = input(prompt)
        try:
            return parse_number(answer)
        except ValueError as error:
            print(f"{error}. Try again.")


def ask_operator(prompt: str) -> Operator:
    while True:
        answer = input(prompt).strip()
        if is_operator(answer):
            return answer
        print(f"{answer!r} is not an operator. Use + - * or /. Try again.")


def run_calculator() -> None:
    first = ask_number("Enter the first number: ")
    op = ask_operator("Enter an operator (+, -, *, /): ")
    second = ask_number("Enter the second number: ")

    try:
        result = calculate(first, op, second)
    except ZeroDivisionError as error:
        print(f"Error: {error}")
    else:
        print(f"{first} {op} {second} = {result}")


def ask_again() -> bool:
    answer = input("calculate again? (y/n): ").strip().lower()
    return answer == "y"


def main() -> None:
    try:
        while True:
            run_calculator()
            if not ask_again():
                break
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
        
