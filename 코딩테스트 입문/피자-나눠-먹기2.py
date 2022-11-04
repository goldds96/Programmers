import math

def lcm(a: int, b: int) -> int :
    return (a * b) // math.gcd(a,b)

def solution(n: int) -> int :
    return lcm(n, 6) // 6