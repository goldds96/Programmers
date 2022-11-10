def solution(array: list, n: int) -> int:
    idx = 0
    delta = 100
    for i in array:
        if abs(i - n) < delta:
            delta = abs(i - n)
            idx = i
            temp = i
        if abs(i - n) == delta:
            if i > temp:
                idx = temp
            else:
                idx = i
    return idx
