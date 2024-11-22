from typing import List

def check_errors(number):
    if number == 0:
        raise Exception("There is no factorial for 0")
    elif number< 0:
        raise Exception("There is no factorial for negative integers")


def get_factorial(number: int) -> int:
    check_errors(number)

    numbers = range(1, number + 1)
    results = 1
    
    # Print table headers
    print(f"{'Step':<10} {'Value':<10}")
    print("-" * 20)

    for number in numbers:
        results *= number
        print(f"Step {number}: {results}")

    return results

factorial = get_factorial(10)
print(factorial)

