def solution(my_string: str) -> str:
    result = ''
    for i in my_string:
        if i.isupper():
            result += i.lower()
        else:
            result += i.upper()
    return result 