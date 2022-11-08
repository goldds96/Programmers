def solution(lines: list) -> int:
    line1 = set()
    line2 = set()
    line3 = set()
    value1 = set()
    value2 = set()
    value3 = set()
    duplicate = set()
    duplicateArray = []
    duplicationCount = 0
    duplicateSum = 0
    result = 0
    mylist = sum(lines, [])

    for i in range(mylist[0], mylist[1]+1):
        line1.add(i)
    for j in range(mylist[2], mylist[3]+1):
        line2.add(j)
    for k in range(mylist[4], mylist[5]+1):
        line3.add(k)

    if len(line1 & line2) > 1:
        value1 = line1 & line2
    if len(line2 & line3) > 1:
        value2 = line2 & line3
    if len(line3 & line1) > 1:
        value3 = line3 & line1
    if len(line1 & line2 & line3) > 1:
        duplicate = line1 & line2 & line3

    if len(value1) > 1:
        list1 = sorted(list(value1))
        result = list1[-1] - list1[0]

    if len(value2) > 1:
        list2 = sorted(list(value2))
        result += list2[-1] - list2[0]

    if len(value3) > 1:
        list3 = sorted(list(value3))
        result += list3[-1] - list3[0]

    if len(duplicate & value1) > 0:
        duplicationCount += 1

    if len(duplicate & value2) > 0:
        duplicationCount += 1

    if len(duplicate & value3) > 0:
        duplicationCount += 1

    if len(duplicate) > 1:
        duplicateArray = sorted(list(duplicate))
        duplicateSum = duplicateArray[-1] - duplicateArray[0]


    print(duplicateSum * (duplicationCount - 1))
    return result - duplicateSum * (duplicationCount - 1)