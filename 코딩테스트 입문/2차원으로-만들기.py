def solution(num_list: list, n: int) -> list:
    result = []
    for i in range(len(num_list) // n):
        result.append(num_list[:n])
        del num_list[:n]
            
    return result
