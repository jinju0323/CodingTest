def solution(my_string, letter):
    # return "".join([char for char in my_string if char not in letter])
    return my_string.replace(letter, '')