def solution(my_string):
    # 대소문자 변환 함수
    # return my_string.swapcase()
    
    # 각 문자가 대문자인지 소문자인지 확인하여 변환 후 하나의 문자열로 합침
    return ''.join([char.lower() 
                    if char.isupper() 
                    else char.upper() 
                    for char in my_string])