from math import floor


def solution(s):
    answer = ""
    strlen = len(s)

    if strlen % 2 == 0:
        mid = int(strlen / 2)
        answer += s[mid - 1] + s[mid]
    else:
        mid = floor(strlen / 2)
        answer += s[mid]

    return answer
