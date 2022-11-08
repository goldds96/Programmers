def solution(my_string: str, num1: int, num2: int) -> str:
    temp = my_string[num1]
    my_string = my_string.replace(my_string[num1], my_string[num2], 1)
    my_string = my_string[:num1+1] + my_string[num1+1:].replace(my_string[num2], temp, 1)

    return my_string