def solution(answers):
    answer = [_ for _ in range(3)]
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in answers:
        if first[i % len(first)] == i:
            answer[0] += 1
        if second[i % len(second)] == i:
            answer[1] += 1
        if third[i % len(third)] == i:
            answer[2] += 1

    highest = max(answer[0], answer[1], answer[2])
    for i in range(3):
        if answer[i] == highest:
            answer.append(i + 1)
    return answer


if __name__ == "__main__":
    print(solution([1, 3, 2, 4, 2]))
