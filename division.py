def divide_numbers(num1:int, num2:int)->float:
    if num2 == 0:
        print('Yoooo!! No zero!!')
        raise ZeroDivisionError("Cannot divide by 0. We refuse!")

    return num1/num2