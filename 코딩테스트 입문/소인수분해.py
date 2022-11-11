def solution(n: int) -> list:
    isPrime = 0
    prime = [2]
    result = []
    
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                isPrime = 0
                break
            else:
                isPrime = 1
        if isPrime: prime.append(i)
    
    for k in prime:
        if n % k == 0:
            result.append(k)
        
    return result
