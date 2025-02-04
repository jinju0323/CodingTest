def solution(age):
    return ''.join(chr(ord('a') + int(num)) for num in str(age))