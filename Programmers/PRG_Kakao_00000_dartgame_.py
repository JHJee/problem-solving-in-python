import re


def solution(dartResult):
    answer = 0
    regex = re.compile("((\d{1,2})(\w{1})(\w{1})){3}$")
    regroups = regex.findall(dartResult)
    print(regroups.group())
    return answer
