def solution(box, n):
    # 각 방향에서 주사위가 몇 개 들어가는지 계산
    a = box[0] // n  # 가로
    b = box[1] // n  # 세로
    c = box[2] // n  # 높이
    
    return a * b * c  # 총 주사위 개수
