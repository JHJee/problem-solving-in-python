def solution(array, commands):
    answer = []
    for index in range(len(commands)):
        i = commands[index][0] - 1
        j = commands[index][1]
        k = commands[index][2] - 1
        tmp_list = array[i:j]
        tmp_list.sort()
        answer.append(tmp_list[k])
    return answer


"""
    Lessons learnt:
        - lambda
        - i, j, k = command
"""
