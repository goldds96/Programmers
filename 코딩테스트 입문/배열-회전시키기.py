def solution(numbers: list, direction: str) -> list:
    result = []
    if direction == "right":
        result.append(numbers[-1])
        for i in range(0, len(numbers)-1):
            result.append(numbers[i])
    else:
        for j in range(1, len(numbers)):
            result.append(numbers[j])
        result.append(numbers[0])
    return result