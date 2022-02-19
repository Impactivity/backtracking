import sys

read = sys.stdin.readline

# 암호는 최소 한개의 모음과 두개의 자음으로 구성한다.
# l은 암호의 길이이고 주어지는 c는 문자의 갯수이다.
# 암호는 오름차순으로 가능한 모든 암호열을 출력한다.

l,c = map(int, read().split())
arr = list(map(str, read().split()))

arr.sort()

visited = [0] * c
s = []

def check(s):
    cnt_a = 0
    cnt_b = 0

    for i in s:
        if i in ['a','e','i','o','u']:
            cnt_a += 1
        else :
            cnt_b += 1

    if cnt_a >= 1 and cnt_b >= 2:
        return True
    else:
        return False

def dfs(len, inx):
    #문자열 append 길이가 l이 될때 까지
    if len == l:
        if check(s) == True:
            print(''.join(s))
        return

    for i in range(inx,c):
        if visited[i] == 0:
            s.append(arr[i])
            visited[i] = 1
            dfs(len+1,i+1) #여기서 inx+1이 아닌 i+1을 해줘야 중복이 나타나지 않는다.
            del s[-1]
            visited[i] = 0

    return

dfs(0,0)


