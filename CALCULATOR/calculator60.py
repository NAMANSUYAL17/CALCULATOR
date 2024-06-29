print("**CALCULATOR**")
import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division
}
def calculator():
    first_number=float(input("Enter your first number:"))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input("pick an operation:")
        second_number=float(input("enter the second number:"))
        calculator_function=operations_dict[op_symbol]
        output=calculator_function(first_number,second_number)
        print(f"{first_number}{op_symbol}{second_number}={output}")
        should_continue=input(f"Type 'y' if you want to continue with {output}, 'n' to start new calculation and 'x' to exit:").lower()
        if should_continue=='y':
            first_number=output
        elif should_continue=='n':
            continue_flag=False
            os.system('cls')
            calculator()
        elif should_continue=='x':
            continue_flag=False
            print("Bye")
calculator()
       