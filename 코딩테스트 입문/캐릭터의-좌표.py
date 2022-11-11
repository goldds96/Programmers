def solution(keyinput: list, board: list) -> list:
    result = [0, 0]
    limitX = board[0] // 2
    limitY = board[1] // 2
    
    for i in keyinput:
        if i == 'right' and (result[0] + 1) <= limitX:
            result[0] += 1
        elif i == 'left' and (result[0] - 1) >= -limitX:
            result[0] -= 1
        elif i == 'up' and (result[1] + 1) <= limitY:
            result[1] += 1
        elif i == 'down' and (result[1] - 1) >= -limitY:
            result[1] -= 1
    
    return result
