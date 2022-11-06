def solution(babbling: list) -> int:
    table = ["aya", "ye", "woo", "ma"]
    count = 0

    for i in babbling:
        for j in table:
            i = i.replace(j, " ")
        # Special case "wyeoo"
        # 1. "wyeoo"에서 ye가 제거되어 "woo"가 됨.
        # 2. "woo"에서 woo가 제거되어 ""가 됨.
        # 이런 경우를 막기 위해 먼저 ' '으로 바꿔준 후 그 후에 공백을 제거
        # 그러면 "wyeoo"에서 ye가 제거되고 "woo"가 아닌 "w oo"가 됨.
        # 따라서 woo가 제거되지 않으므로 count 되지 않음.
        i = i.replace(" ", "")
        if len(i) == 0:
            count += 1

    return count
