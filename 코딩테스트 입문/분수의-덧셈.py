import math

def lcm(a: int, b: int) -> int :
    return (a * b) // math.gcd(a,b)

def solution(denum1: int, num1: int, denum2: int, num2: int) -> list :
    answer = []
    if num1 == num2:
        answer.append(denum1 + denum2)
        answer.append(num1)
    else:
        mylcm = lcm(num1, num2)
        answer.append((mylcm // num1) * denum1 + (mylcm // num2) * denum2)
        answer.append(mylcm)
    while(math.gcd(answer[0], answer[1]) != 1):
        divisor = math.gcd(answer[0], answer[1])
        answer[0] = answer[0] // divisor
        answer[1] = answer[1] // divisor
    return answer