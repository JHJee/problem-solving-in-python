import heapq as hq


def solution(h, K):
    answer = 0
    hq.heapify(h)
    while h[0] < K:
        if len(h) == 1 and h[0] < K:
            answer = -1
            break
        first = hq.heappop(h)
        second = hq.heappop(h)
        new = first + (second * 2)
        hq.heappush(h, new)
        answer += 1

    return answer
