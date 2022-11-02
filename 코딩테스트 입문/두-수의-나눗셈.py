def solution(num1: int, num2: int) -> int :
    assert num1 and num2 in range(1, 101)
    return int(num1 / num2 * 1000)