def solution(box: list, n: int) -> int:
    result = 1
    for i in box:
        result *= i // n
    return result