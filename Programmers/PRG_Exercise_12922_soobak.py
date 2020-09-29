def solution(n):
    answer = ""
    for i in range(n):
        if i % 2:
            answer += "박"
        else:
            answer += "수"
    return answer


""" # Alternative Code
def solution(n):
    return "수박"*(n//2) + "수"*(n%2)
"""
