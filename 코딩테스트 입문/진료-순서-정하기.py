def solution(emergency: list) -> list:
    result = []
    mylist = sorted(emergency, reverse=True)
    for i in emergency:
        result.append(mylist.index(i) + 1)
    return result
