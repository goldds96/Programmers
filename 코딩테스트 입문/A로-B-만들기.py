def solution(before: str, after: str) -> int:
    for i in before:
        if i not in after:
            return 0
        else:
            after = after.replace(i, '', 1)
    return 1
