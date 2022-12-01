def solution(my_string: str) -> int:
    result = 0
    add_flag = True
    my_list = my_string.split()
    
    for i in my_list:
        if i.isdigit():
            if add_flag:
                result += int(i)
                add_flag = False
            else:
                result -= int(i)
        else:
            if i == '+':
                add_flag = 1
            else:
                add_flag = 0
    
    return result
