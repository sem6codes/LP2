def is_safe(board, x, y, n):
    for i in range(x):
        if board[i][y] or (y - x + i >= 0 and board[i][y - x + i]) or (y + x - i < n and board[i][y + x - i]):
            return False
    return True

def solve(board, x, n):
    if x == n:
        return True
    for y in range(n):
        if is_safe(board, x, y, n):
            board[x][y] = 1
            if solve(board, x + 1, n):
                return True
            board[x][y] = 0
    return False

def main():
    n = int(input("Enter number of Queens: "))
    board = [[0]*n for _ in range(n)]
    if solve(board, 0, n):
        for row in board:
            print(*row)

if __name__ == '__main__':
    main()
