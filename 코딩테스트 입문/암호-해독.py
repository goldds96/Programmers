def solution(cipher: str, code: int) -> str:
    plain = ''
    for i in range(code-1, len(cipher), code):
        plain += cipher[i]
    return plain