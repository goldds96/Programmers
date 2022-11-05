def solution(numbers: list) -> int:
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]
