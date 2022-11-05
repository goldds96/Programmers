def solution(my_string: str, n: int) -> str:
    result = ""
    my_list = list(my_string)
    for i in my_list:
        result += i * n
    return result
