import random
from addition import add_numbers
from substraction import substract_numbers
from multipication import multiply_numbers
from division import divide_numbers


def get_random_int():
    rand = random.randint(5, 10)
    return rand

def show_results(num1:int, num2:int, results: float, operation: str):
    print(f'{num1} {operation} {num2} = {results}')
    
num1 = get_random_int()
num2 = get_random_int()

addition_res = add_numbers(num1, num2)
show_results(num1, num2, addition_res, "+")

substarction_res = substract_numbers(num1,num2)
show_results(num1, num2,substarction_res, '-')

multiply_res = multiply_numbers(num1, num2)
show_results(num1,num2, multiply_res,'x')

divivion_res1 = divide_numbers(num1, num2)
show_results(num1, num2, divivion_res1,'/')

divivion_res2 = divide_numbers(num1, 0)
show_results(num1,0, divivion_res2,'/')

