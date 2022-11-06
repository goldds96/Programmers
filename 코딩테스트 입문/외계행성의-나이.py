import string


def solution(age: int) -> str:
    result = ""
    mylist = list(str(age))
    for i in mylist:
        result += string.ascii_lowercase[int(i)]
    return result
