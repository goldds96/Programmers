def solution(s: str) -> int:
    temp = 0
    result = 0
    my_list = s.split()
    
    for i in my_list:
        try:
            result += int(i)
        except:
            result -= temp
            
        if i == 'Z':
            temp = temp
        else:
            temp = int(i)
    
    return result
