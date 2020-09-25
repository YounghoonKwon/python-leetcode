import sys
sys.stdin = open("input.txt", "r")
location = sys.stdin.readline()
x = ord(location[0]) - ord('a') + 1
y = int(location[1])
dx = [1,-1,1,-1,2,2,-2,-2]
dy = [2,2,-2,-2,1,-1,1,-1]
count = 0
for i in range(8):
    nx = x+dx[i]
    ny = y+dy[i]
    if nx >= 1 and ny >= 1 and nx <=8 and ny <=8:
        count += 1
print(count)


