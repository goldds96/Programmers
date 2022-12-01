def solution(common: list) -> int:
  number = common[-2] - common[-3]
  if common[-2] + number == common[-1]:
    return common[-1] + number
  return common[-1] * (common[-2] // common[-3]
