def solution(my_string: str) -> str:
    table = ["a", "e", "i", "o", "u"]
    result = ""
    for i in my_string:
        for j in table:
            i = i.replace(j, '')
        result += i
    return result