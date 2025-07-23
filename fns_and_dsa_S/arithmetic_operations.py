"""
0. Arithmetic Operations Function mandatory

Create a Python script named arithmetic_operations.py. In this script, define a function that performs basic arithmetic operations. This function, perform_operation, will be imported and used in a separate main.py script, which we provide.

Requirements for arithmetic_operations.py:
Function Definition:
Define a function named perform_operation.
Parameters: num1 (float), num2 (float), and operation (string). The operation parameter accepts four possible values: 'add', 'subtract', 'multiply', or 'divide'.
The function should execute the arithmetic operation based on the operation parameter and the numerical values provided.
For division, include handling for division by zero, returning a specific message or value that your main.py script can recognize and display appropriately.
Return the result of the arithmetic operation.

"""
#function declaration
def perform_operation(num1, num2, operation):

#for debugging purposes
    print(f"num1 = {num1}")
    print(f"num2 = {num2}")
    print(f"operation = {operation}")

#----------------------------------------------------------------------
#if-elif-else implementation of problem statement - start 
#----------------------------------------------------------------------
    if operation == "add" or operation == "+" or operation == "a":
        print("add")
        return num1 + num2
        pass
    elif operation == "subtract" or operation == "-" or operation == "s":
        print("subtract")
        return num1 - num2
        pass
    elif operation == "multiply" or operation == "*" or operation == "m":
        print("multiply")
        return num1 * num2
        pass
    elif operation == "divide" or operation == "/" or operation == "d" and num2 != 0:
        print("divide")
        return num1 / num2
        pass
    elif operation == "divide" or operation == "/" or operation == "d" and num2 == 0:
        print("divide by zero")
        message = "You cannot divide by 0"
        return message
        # return "You cannot divide by 0"
        pass
#if-elif-else implementation of problem statement - end

#------------------------------------------------------------
# Match-Case implementation of the problem statement - start
# -----------------------------------------------------------
    # match operation:
    #     case "add" | "+" | "a":
    #         return num1 + num2
    #     case "subtract" | "-" | "s":
    #         return num1 - num2
    #     case "multiply" | "*" | "m":
    #         return num1 * num2
    #     case "divide" | "/" | "d":
    #         if num2 != 0:
    #             return num1 / num2
    #         else:
    #             return "You cannot divide by 0"
                # divide_by_zero_error_message = "You cannot divide by 0"
                # return divide_by_zero_error_message    
# Match-Case implementation of the problem statement - end
    
#----------------------------------------------------------
#Testing my code
#---------------------------------------------------------
result = perform_operation(1,9,"a")
print(result)