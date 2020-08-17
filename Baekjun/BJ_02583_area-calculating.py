# Python3
# BJ #2583
# BFS

M, N, K = map(int, input().split())
board = [[0 for _ in range(N)] for _ in range(M)]


def color_board(Lx, Ly, Rx, Ry):
    for i in range(Lx, Rx):
        for j in range(Ly, Ry):
            board[j][i] = 1


for i in range(K):
    Lx, Ly, Rx, Ry = map(int, input().split())
    color_board(Lx, Ly, Rx, Ry)


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(start):
    queue = [start]
    square = 1
    board[start[0]][start[1]] = 2
    while queue:
        point = queue.pop()

        for i in range(4):
            nx = point[0] + dx[i]
            ny = point[1] + dy[i]
            if (
                (0 <= nx)
                and (nx < M)
                and (0 <= ny)
                and (ny < N)
                and (board[nx][ny]) == 0
            ):
                board[nx][ny] = 2
                square += 1
                queue.append((nx, ny))
    return square


LST = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            LST.append(bfs((i, j)))

print(len(LST))
LST.sort()
for i in LST:
    print(i, end=" ")
