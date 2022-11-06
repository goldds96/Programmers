import math

def solution(balls: int, share: int) -> int:
    return math.factorial(balls) / (math.factorial(balls - share) * math.factorial(share))