import sys
read = sys.stdin.readline

sudoku = [ list(map(int, read().split())) for _ in range(9)]

blank = []

#blank되어있는 값들 append
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i,j))


# 가로행과 세로열 그리고 3x3 박스 세 가지 체크를 해야함.
def dfs(inx):
    if inx == len(blank):
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end = ' ')
            print(' ')
        exit(0)

    for i in range(1,10):
        x = blank[inx][0]
        y = blank[inx][1]

        if check(x,y,i):
            sudoku[x][y] = i
            dfs(inx+1)
            sudoku[x][y] = 0


def check(x,y,num):
    #가로, 세로 줄 체크
    for i in range(9):
        if num == sudoku[i][y]:
            return False
        if num == sudoku[x][i]:
            return False

    # 3x3 사각형 체크
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if num == sudoku[nx + i][ny + j]:
                return False
    return True



dfs(0)
