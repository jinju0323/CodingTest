def solution(array):
    # 빈 딕셔너리로 숫자별 등장 횟수 기록
    freq = {}
    
    # 배열에서 하나씩 꺼내서 등장 횟수 세기
    for num in array:
        if num in freq:  # 이미 등장한 숫자라면
            freq[num] += 1  # 횟수 1 증가
        else:  # 처음 등장한 숫자라면
            freq[num] = 1  # 횟수 1로 시작

    # 가장 많이 나온 횟수 구하기
    max_freq = 0
    for count in freq.values():
        if count > max_freq:
            max_freq = count  # 최빈값의 횟수 찾기

    # 최빈값 구하기
    most_frequent = []
    for key, value in freq.items():
        if value == max_freq:  # 횟수가 가장 큰 숫자 찾기
            most_frequent.append(key)

    # 최빈값이 하나만 있으면 그 숫자 반환, 여러 개 있으면 -1 반환
    if len(most_frequent) == 1:
        return most_frequent[0]
    else:
        return -1