import re

def solution(my_string: str) -> int:
    return sum([int(i) for i in re.sub(r'[^1-9]', '', my_string)])