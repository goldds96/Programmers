import re

def solution(my_string: str) -> int:
    list = re.sub('[A-Z | a-z]', ' ', my_string).split(' ')
    return sum(int(i) for i in list if i.isdigit())
