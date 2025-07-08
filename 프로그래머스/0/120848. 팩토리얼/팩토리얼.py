def solution(n):
    i = 1
    answer = 1
    while answer <= n:
        i += 1
        answer *= i
    return i - 1
   
