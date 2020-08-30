from collections import deque

"""     board         reversed       new_board
    [ 0 0 0 0 0 ]	[ 3 5 1 3 1 ]	[[3 4     ],
    [ 0 0 1 0 3 ]	[ 4 2 4 4 2 ]	 [5 2 2   ],
    [ 0 2 5 0 1 ] =>[ 0 2 5 0 1 ] => [1 4 5 1 ],
    [ 4 2 4 4 2 ]	[ 0 0 1 0 3 ]	 [3 4     ],
    [ 3 5 1 3 1 ]	[ 0 0 0 0 0 ]	 [1 2 1 3 ]]
"""


def solution(board, moves):
    blen = len(board)
    board.reverse()
    new_board = [[] for _ in range(blen)]
    basket = []
    for index in range(blen):
        for li in range(blen):
            val = board[li][index]
            if val == 0:
                break
            else:
                new_board[index].append(val)
    moves = deque(moves)
    answer = 0
    for _ in range(len(moves)):
        index = moves.popleft() - 1
        if new_board[index]:  # if not empty column
            basket.append(new_board[index].pop())
            if len(basket) > 1 and basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2
    return answer
