from collections import deque

def solution(numbers: list, k: int) -> int:
    numbers = deque(numbers)
    numbers.rotate(-2 * (k-1))
    numbers = list(numbers)

    return numbers[0]
