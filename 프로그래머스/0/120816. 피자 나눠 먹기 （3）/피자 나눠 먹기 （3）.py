def solution(slice, n):
    answer = 0  # 결과값을 저장할 변수 초기화
    
    if n % slice == 0:  # 나누어 떨어지는 경우
        answer = n // slice  # 몫만 반환
    else:  # 나머지가 있는 경우 (즉, 더 필요한 판이 있는 경우)
        answer = n // slice + 1  # 몫에 1을 더해서 반환
    
    return answer