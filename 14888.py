import sys
read = sys.stdin.readline
def dfs(cnt, result, p, m, mul, div):
    global max_result
    global min_result
    if cnt == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if p:
        dfs(cnt + 1, result + s[cnt], p - 1, m, mul, div)
    if m:
        dfs(cnt + 1, result - s[cnt], p, m - 1, mul, div)
    if mul:
        dfs(cnt + 1, result * s[cnt], p, m, mul - 1, div)
    if div:
        dfs(cnt + 1, -(-result // s[cnt]) if result < 0 else result // s[cnt], p, m, mul, div - 1)


n = int(read())
s = list(map(int, read().split()))
op = list(map(int, read().split()))
max_result = -1000000001
min_result = 1000000001
dfs(1, s[0], op[0], op[1], op[2], op[3])
print(max_result)
print(min_result)






# 오답 코드
# import sys
# read = sys.stdin.readline
# N = int(read())
# A = list(map(int, read().split()))
# calc = list(map(int, read().split()))
#
# _sum = A[0]
# answer = []
#
# #직전 계산에 덧셈, 뺄셈, 곱셈, 나눗셈
# def dfs(inx):
#
#     global _sum
#
#     if inx == N-1:
#         answer.append(_sum)
#         return
#
#     if calc[0] > 0 : #덧셈
#         _sum += A[inx]
#         calc[0] -= 1
#         dfs(inx+1)
#
#     if calc[1] > 0 :
#         _sum -=  A[inx]
#         calc[1] -= 1
#         dfs(inx + 1)
#
#     if calc[2] > 0 :
#         _sum = _sum * A[inx]
#         calc[2] -= 1
#         dfs(inx + 1)
#
#     if calc[3] > 0 :
#         if _sum < 0 :
#             _sum = -( -_sum // A[inx])
#         else:
#             _sum = _sum // A[inx]
#         calc[3] -= 1
#         dfs(inx + 1)
#
#
# dfs(0)
# print(max(answer))
# print(min(answer))
