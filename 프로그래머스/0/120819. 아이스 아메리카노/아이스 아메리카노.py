def solution(money):
    price = 5500
    americano = money // price
    m = money % price
    return [americano, m]