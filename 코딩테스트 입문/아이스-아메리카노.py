def solution(money: int) -> int:
    result = []
    result.append(money // 5500)
    result.append(money % 5500)
    return result