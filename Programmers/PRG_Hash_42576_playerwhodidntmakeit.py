def solution(participant, completion):
    answer = ""
    partlen = len(participant)
    participant.sort()
    completion.sort()
    newdict = {}
    for i in range(0, partlen):
        newdict[participant[i]] = ""

    for i in range(0, partlen):
        if i == partlen - 1:
            answer = participant[i]
            break
        if participant[i] == completion[i]:
            pass
        else:
            answer = participant[i]
            break
    return answer


"""
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
"""
