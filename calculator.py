import math
from typing import Literal

Operator = Literal["+", "-","*", "/"]

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


def ask_number(prompt: str) -> float:
    while True:
        answer = input(prompt)
        try:
            return parse_number(answer)
        except ValueError as error:
            print(f"{error}. Try again.")

first = ask_number("Enter the first number: ")
print(f"{first} ({type(first).__name__})")