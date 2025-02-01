def solution(num_list):
    # 파이썬 기능
    # num_list.reverse()
    # return num_list
    
    # 리스트 슬라이싱
    # return num_list[::-1]
    
    # 투 포인터
    n = len(num_list)
    for i in range(n//2):
        p = n - i - 1
        num_list[i], num_list[p] = num_list[p], num_list[i]
        
    return num_list 