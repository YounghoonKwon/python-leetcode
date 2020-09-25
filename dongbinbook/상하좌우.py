import sys
sys.stdin = open("input.txt", "r")
N = int(sys.stdin.readline())
steps = list(sys.stdin.readline().split())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']
x = 1
y = 1
for step in steps:
    for i in range(len(move_types)):
        if step == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    if nx >= 1 and ny >= 1 and nx <=N and ny<=N:
        x = nx
        y = ny

print(x,y)

