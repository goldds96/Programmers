def solution(s1: list, s2: list) -> int:
    count = 0
    for i in s1:
        if i in s2:
            count += 1
    return count