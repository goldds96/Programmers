def solution(array: list) -> int :
    count = []
    iterList = list(set(array))     # Remove duplication
    for i in iterList:
        count.append(array.count(i))
    indexList = [index for index, value in enumerate(count) if value == max(count)]
    if len(indexList) == 1: 
        return iterList[indexList[0]]
    else: 
        return -1
