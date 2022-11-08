from itertools import combinations

def solution(numbers: list) -> int:
    mylist = list(combinations(numbers,2))
    result = []
    
    for i in mylist:
        result.append(i[0] * i[1])
    
    return max(result)