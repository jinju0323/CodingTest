def solution(emergency):
    se = sorted(emergency, reverse=True)
    answer = [se.index(e) + 1 for e in emergency]
    return answer