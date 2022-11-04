def solution(array: list, height: int) -> int:
    cnt = 0
    for i in array:
        if i > height:
            cnt += 1
    return cnt