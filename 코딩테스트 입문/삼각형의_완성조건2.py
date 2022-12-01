def solution(sides: list) -> int:
    count1 = set()
    count2 = set()
    sides.sort()
    
    for i in range(1, sides[1]+1):
        if i + sides[0] > sides[1]:
            count1.add(i)
            
    for i in range(max(sides)+1, sum(sides)+1):
        if i < sum(sides):
            count2.add(i)
    
    return len(count1.union(count2))
