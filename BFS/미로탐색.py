#https://www.acmicpc.net/problem/2178
"""
알고리즘 설명
최단거리를 찾는 문제이므로 BFS를 사용해야 한다.
BFS는 너비 우선 탐색으로 시작점과 인접한 노드들을 탐색하며 정답을 찾는 방법이다.
큐 구조를 이용하여 큐에 노드의 위치를 담고 큐에서 꺼낸 노드 근처의 노드들을 검사하며 정답을 찾는다.
나는 현재 미로의 배열에서 이동한 인덱스가 늘어남에 따라 인접 인덱스를 자기 기준 위치의 값에 +1하는 방식으로 진행하였다.

1. [Y][X]이며 시작점 위치는 [0,0]이고 도착점 위치는 [a,b]이다
    좌표에서 헷갈리지 않게 y가 증가할수록 눈으로 보는 위치는 아래로 내려간다. 즉 첫번째로 받은 리스트를 y가 0 그다음이 1, 그다음이 2... 이렇게 커질수록 위치는 내려간다
2. 큐는 deque로 설정하여 복잡도를 줄인다. 큐에 첫 인덱스에는 초기위치인 [0,0]을 넣는다.
3. 총 반복은 queue의 길이가 다 떨어질 때 까지이다. 
    1) 현재 위치에 큐의 popleft()한 값을 넣는다.
    2) 그거를 토대로 현재 위치의 x,y 좌표를 설정한다
    3) 현재 위치에 인접한 노드들을 검사한다. 내 위치에서 4방면(위,아래,왼쪽,오른쪽)을 확인한다. 만약 내 위치에서 인접한 노드가 내가 갔던 길이 아니라면 그 노드의 위치를 큐에 넣고
       큐에 넣은 노드의 값을 자신의 값 + 1을 한다.
4. 만약 꺼낸 큐의 위치가 정답 위치이면 바로 종료한다.
"""
from collections import deque 
q = deque()
a,b = list(map(int,input().split()))
miro = []
for _ in range(a):
    miro.append(list(map(int, input())))
q.append([0, 0])
while len(q) > 0:
    now_location = q.popleft()
    now_y = now_location[0]
    now_x = now_location[1]
    if now_y == a and now_x == b:
        break
    #왼쪽 이동 가능하다면
    if now_x - 1 > -1 and miro[now_y][now_x-1] == 1:
        q.append([now_y, now_x-1])
        miro[now_y][now_x-1] = miro[now_y][now_x]+1
    #오른쪽 이동 가능하다면
    if now_x + 1 < b and miro[now_y][now_x+1] == 1:
        q.append([now_y, now_x+1])
        miro[now_y][now_x+1] = miro[now_y][now_x]+1
    #위로 이동 가능하다면
    if now_y -1 > -1 and miro[now_y-1][now_x] == 1:
        q.append([now_y-1, now_x])
        miro[now_y-1][now_x] = miro[now_y][now_x]+1
    #아래로 이동 가능하다면
    if now_y + 1 < a and miro[now_y+1][now_x] == 1:
        q.append([now_y+1, now_x])
        miro[now_y+1][now_x] = miro[now_y][now_x]+1

print(miro[a-1][b-1])