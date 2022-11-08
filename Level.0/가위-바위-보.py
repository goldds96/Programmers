def solution(rsp: str) -> str:
    table = ["2", "0", "5", "2"]
    return "".join(table[table.index(i) + 1] for i in list(rsp))

