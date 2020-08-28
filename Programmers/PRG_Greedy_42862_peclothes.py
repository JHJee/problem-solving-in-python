def solution(n, lost, reserve):
    left = 0
    right = 0
    count = len(lost)
    for i in range(1, n + 1):
        if i in lost and i in reserve:
            reserve.remove(i)
            lost.remove(i)
            count -= 1
    for i in lost:
        if i > 1:
            left = i - 1
        if i < n:
            right = i + 1
        if left != 0 and (left in reserve):
            reserve.remove(left)
            count -= 1
        elif right != 0 and (right in reserve):
            reserve.remove(right)
            count -= 1
    return n - count
