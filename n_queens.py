def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'Q' or (col - row + i >= 0 and board[i][col - row + i] == 'Q') or (col + row - i < n and board[i][col + row - i] == 'Q'):
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        for line in board:
            print(' '.join(line))
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q' # place the queen
            solve_n_queens(board, row + 1, n)
            board[row][col] = '.' # backtrack

n = 4
board = [['.']*n for _ in range(n)]

solve_n_queens(board, 0, n)
