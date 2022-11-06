def solution(hp: int) -> int:
    result = hp // 5
    remainder = hp % 5

    result += remainder // 3
    remainder %= 3

    result += remainder // 1
    remainder %= 1

    return result
