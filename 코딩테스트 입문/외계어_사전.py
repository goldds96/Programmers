def solution(spell: list, dic: dict) -> int:
    for i in list(dic):
        for j in sorted(spell):
            if j in i:
                i = i.replace(j, ' ', 1)
            else:
                break
        if i.count(' ') == len(spell):
            return 1
    return 2
