def solution(my_string):
    # 숫자만 저장할 리스트 생성
    numbers = []
    
    # 문자열을 한 글자씩 순회
    for char in my_string:
        # 현재 문자가 숫자인지 확인
        if char.isdigit():
            # 숫자로 변환하여 리스트에 추가
            numbers.append(int(char))
    
    # 숫자 리스트를 오름차순 정렬하여 반환
    return sorted(numbers)