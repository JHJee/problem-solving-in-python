def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr1[0])
    answer = [0] * row
    for i in range(row):
        answer[i] = [0] * col

    for i in range(row):
        for j in range(col):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer
