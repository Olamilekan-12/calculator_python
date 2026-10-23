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


answer = input("Enter the first number: ")
first = parse_number(answer)
print(f"{first} ({type(first).__name__})")