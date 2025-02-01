def solution(n):
    answer = 0
    x = int(n ** 0.5)
    if x * x == n:
        answer = 1
    else:
        answer = 2
    return answer