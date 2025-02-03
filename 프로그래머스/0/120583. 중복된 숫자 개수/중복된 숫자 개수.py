def solution(array, n):
    # return array.count(n)
    count = 0
    for num in array:
        if num == n:
            count += 1
    return count