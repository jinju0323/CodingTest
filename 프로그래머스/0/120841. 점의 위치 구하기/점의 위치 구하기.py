def solution(dot):
    x, y = dot  # x, y 좌표 추출 (언패킹)

    if x > 0 and y > 0:
        return 1  # 제1사분면
    elif x < 0 and y > 0:
        return 2  # 제2사분면
    elif x < 0 and y < 0:
        return 3  # 제3사분면
    else:
        return 4  # 제4사분면
