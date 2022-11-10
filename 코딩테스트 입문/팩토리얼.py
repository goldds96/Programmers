import math

def solution(n: int) -> int:
    if n == 0 or n == 1: return 1
    for i in range(n+1):
        if math.factorial(i) == n:
            return i
        elif math.factorial(i) > n:
            return i-1
