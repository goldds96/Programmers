def solution(i: int, j: int, k: int):
    return sum([str(i).count(str(k)) for i in range(i, j+1)])
