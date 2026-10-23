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


print(calculate(10, "+", 4))
print(calculate(10, "-", 4))
print(calculate(10, "*", 4))
print(calculate(10, "/", 4))