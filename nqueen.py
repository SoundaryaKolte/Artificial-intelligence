def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_one_n_queen(n):
    def backtrack(row):
        if row == n:
            return True
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                if backtrack(row + 1):
                    return True
        return False

    board = [-1] * n
    if backtrack(0):
        return board
    else:
        return None

def print_one_solution(board):
    if board is None:
        print("No solution exists.")
    else:
        n = len(board)
        for i in board:
            print("." * i + "Q" + "." * (n - i - 1))

# ---- MAIN ----
n = int(input("Enter N (number of queens): "))
solution = solve_one_n_queen(n)
print("\nOne solution:")
print_one_solution(solution)
