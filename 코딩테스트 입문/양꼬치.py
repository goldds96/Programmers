def solution(n: int, k: int) -> int:
    service = n // 10
    return n * 12000 + (k - service) * 2000