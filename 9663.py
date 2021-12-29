import sys

def logic(n):
    if n == N:
        global cnt
        cnt += 1
    else :
        for i in range(N):
            if visited[i] :
                continue

            board[n] = i # n,i 에 퀸 올려놓기

            if check(n): #현재 올려놓은 대상과 이미 올려놓은 퀸들이 대각선상, 같은선상에 존재하는지 체크
                visited[i] = True
                logic(n+1) # 다음행으로
                visited[i] = False

# 대각선에 위치해있다는 조건
# 행끼리의 차와 열끼리의 절대값 차가 같으면 대각선상임..
def check(n):
    for i in range(n):
        # 같은 열에 있거나 같은 대각선에 존재할 때
        if (board[n] == board[i]) or (n - i == abs(board[n]- board[i])):
            return False

    return True


read = sys.stdin.readline
N = int(read())

cnt = 0

#인덱스값이 행이고 배열의 값 열로 저장.
board = [0 for _ in range(N)]
visited = [False for _ in range(N)]

logic(0)
print(cnt)
