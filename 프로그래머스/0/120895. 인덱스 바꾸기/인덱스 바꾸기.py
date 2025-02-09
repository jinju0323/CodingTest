def solution(my_string, num1, num2):
    # 문자열을 리스트로 변환
    s = list(my_string)
    
    # 두 인덱스의 문자 교환
    s[num1], s[num2] = s[num2], s[num1]
    
    # 리스트를 문자열로 변환하여 반환
    return ''.join(s)