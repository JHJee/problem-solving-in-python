# Python3
# BJ #11399
# Greedy
n = input()
input_str = input()
q = list(map(int, input_str.split()))
q.sort()

total = 0
for i in range(0, len(q)):
    for j in range(0, i + 1):
        total += q[j]

print(total)
