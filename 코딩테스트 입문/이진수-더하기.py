def solution(bin1: str, bin2: str) -> str:
    return bin(int(bin1, 2) + int(bin2, 2))[2:]
