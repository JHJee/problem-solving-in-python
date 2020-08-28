def solution(s):
    answer = True
    s = list(s)
    slen = len(s)
    if slen == 4 or slen == 6:
        for item in s:
            if ord(item) <= 47 or ord(item) >= 58:
                answer = False
    else:
        return False
    return answer


"""
    (Improved ver.)
    return s.isdigit() and len(s) in (4, 6)
"""
