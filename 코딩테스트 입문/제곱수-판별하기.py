import math

def solution(n: int) -> int:
    root = math.sqrt(n)
    if (root - int(root) == 0):
        return 1
    return 2