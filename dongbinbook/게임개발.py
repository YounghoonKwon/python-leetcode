import sys
sys.stdin = open("input.txt", "r")
mapx, mapy = map(int, sys.stdin.readline().split())
x,y,dir = map(int, sys.stdin.readline().split())
map = list(list(map(int, sys.stdin.readline().split())) for _ in range(mapx))
# 북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turnleft():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3
count = 0
turncount = 0
while True:
    turnleft()
    nx = x+dx[dir]
    ny = y+dy[dir]
    # if nx < 0 or nx >= mapx or ny < 0 or ny >= mapy:
    #     continue
    if map[nx][ny] == 0:
        x = nx
        y = ny
        count += 1
        turncount = 0
        map[nx][ny] = 9
        continue
    else:
        turncount += 1

    if turncount == 4:
        nx = x-dx[dir]
        ny = y-dy[dir]
        if nx < 0 or nx >= mapx or ny < 0 or ny >= mapy:
            continue
        if map[nx][ny] == 0 or map[nx][ny] == 9:
            x = nx
            y = ny
            turncount = 0
        else:
            break
print(count)








