from typing import List


def get_factorial_from_ls(digits: List[int]) -> int:
    print("list:", digits)

    results = 1
    for digit in digits:
        results = results * digit

    return results

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
factorial_res = get_factorial_from_ls(numbers)
print(factorial_res)