def solution(my_string: str) -> list:
    return sorted([int(i) for i in my_string if i.isdigit()])