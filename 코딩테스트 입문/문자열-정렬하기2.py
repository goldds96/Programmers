def solution(my_string: str) -> str:
    return ''.join(sorted([i.lower() for i in my_string]))