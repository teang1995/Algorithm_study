cnt = 0
moves = []
def hanoi(n, fromm, between, to):
    global moves
    global cnt
    if n == 1:
        cnt += 1
        moves.append(str(fromm) + " " + str(to))
        return
    else:
        hanoi(n - 1, fromm, to, between)
        moves.append(str(fromm) + " " + str(to))
        cnt += 1
        hanoi(n-1, between, fromm, to)
    return cnt
n = int(input())
cnt= hanoi(n, 1, 2, 3)
print(cnt)
for move in moves:
    print(move)
