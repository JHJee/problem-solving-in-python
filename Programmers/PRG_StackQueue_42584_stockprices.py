def solution(prices):
    prlen = len(prices)
    answer = [0 for _ in range(prlen)]
    for i in range(0, prlen):
        for j in range(i + 1, prlen):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
            if j == prlen - 1:
                answer[i] = j - i
    return answer
