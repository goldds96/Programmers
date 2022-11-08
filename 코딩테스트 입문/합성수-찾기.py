def solution(n: int) -> int:
    count = 0
    prime = 1
    
    for i in range(1, n+1):
        for j in range(2, i):
            if i % j == 0:
                prime = 0
                break
            else:
                prime = 1
        if prime:
            print(i)
            count += 1
    
    return n - count
            