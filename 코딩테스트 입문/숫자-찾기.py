def solution(num: int, k: int) -> int:
    for i in list(str(num)):
        if i == str(k):
            return list(str(num)).index(i)+1
    return -1