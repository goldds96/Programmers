def solution(dots: list) -> int:
    gradient1 = []
    gradient2 = []

    for i in range(1, 4):
        gradient1.append((dots[i][1] - dots[0][1]) / (dots[i][0] - dots[0][0]))

    gradient2.append((dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0]))
    gradient2.append((dots[3][1] - dots[1][1]) / (dots[3][0] - dots[1][0]))
    gradient2.append((dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0]))

    for i in gradient1:
        if i in gradient2:
            return 1

    return 0
