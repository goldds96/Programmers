def solution(num_list: list) -> list:
    odd = 0
    even = 0
    result = []
    for i in num_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    result.append(even)
    result.append(odd)
    return result