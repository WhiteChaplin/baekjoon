#https://www.acmicpc.net/problem/1260
"""
https://hongcoding.tistory.com/78
그래프라는 자료구조에 대한 개념을 알아야 하는 문제였다.
인접행렬을 만들어 해당 노드끼리 연결되어 있다면 1을 넣고 아니면 0을 넣는다.
이 인접행렬을 토대로 이어져 있는 노드인지 아닌지 파악해서 문제를 풀면 된다.

필요한 변수
1. 정점과 간선의 갯수 및 시작위치를 담는 변수
2. 인접행렬을 저장해둔 변수
3. 이 노드가 방문했는지 안했는지 확인하는 리스트 변수
4. 방문 순서를 담는 리스트 변수


dfs 알고리즘 설명
dfs 깊이 우선 탐색이라 하나의 경우의 수에 대해 모든 경우의 수를 찾고 없다면 그 다음으로 넘어가는 방식이다
즉, 여기서는 시작노드와 인접해 있는 것을 찾아보고 만약 있다면 그 노드로 이동한다. 문제에도 나왔듯이 갈수있는 노드가 여러개이면 제일 숫자가 낮은 노드부터 방문인다.
그렇게 노드를 이동해가며 방문한 노드의 순서를 출력하면 된다.
dfs가 좀 코드를 다시짜고 그랬는데 처음에는 반복문을 돌렸다. 노드의 총 갯수로. 근데 생각해보니 시작 노드를 옮겨다니면서 검사를 해야한다는 것을 깨달았다.
반복문으로는 노드를 옮길 수 있으겠으나 코드가 굉장히 지저분하고 필요없는 반복과 변수들이 생길 거 같아 생각해보니 재귀함수를 사용하여 시작 노드를 옮기면 될 거 같다는 생각이 들었다.
그래서 재귀함수로 호출하며 반복을 진행하였고, 호출하면서 방문한 노드를 리스트에 추가하였다.
1. 시작함수를 인자로 받는 dfs함수를 생성한다
2. 방문했는지 확인하는 리스트인 visit_node의 시작위치를 1로 설정하여 방문했다는 표시를 한다
3, for문을 돌린다. 이때 인접행렬을 이용한다. 만약 현재 노드에서 갈 수 있는 노드가 있는데 for문을 돌리는거라 제일 낮은 것부터 돌리기 떄문에 자동으로 낮은 것부터 시작하게 된다.
   for문을 돌리다가 만약 방문하지 않는 노드이고(visit_node가 0) 인접행렬을 토대로 이어져 있는 노드라면 현재 노드를 방문한 노드로 변경하고 start를 for문에 i번호로 주어
   재귀함수롤 다시 호출한다. 
4. 만약 모든 노드를 다 돌았으면(모든 재귀가 끝나면) for문과 if문이 적용이 되지 않아 반복을 마치게 되고 방문 순서를 담은 리스트 변수(visit_node)를 출력한다


bfs 알고리즘 설명
bfs 너비 우선 탐색이라 하나의 경우에 수에 대해 모든 다음 경우의 수를 조사하며 탐색하는 방식이다. 큐를 이용한다.
즉, 여기서는 시작노드와 인접해 있는 노드들을 모두 탐색하고, 숫자가 적은 노드부터 탐색을 시작한다.
0. 총 반복 횟수는 큐에 길이가 0까지이다. 시작할 때 큐에 start 노드를 넣는다. 방문 노드(visit_node) 역시 시작값을 넣는다.(1로 설정)
while문 시작
1. 현재 큐에 담겨있는 것 중 leftpop()을 한다. 그것이 현재 노드이다.
2. for문과 인접행렬을 이용해 현재 노드와 연결되어 있는 노드들을 큐에 담는다.
3. 2번에서 큐에 담은 노드들을 전부 방문 노드(visit_node)에 방문했다고 설정하고 방문 순서 리스트(visit_list)에 담는다.
4. while문 조건이 만족할 때 까지 반복한다. 만약 큐에 길이가 0이면 종료하고 방문 순서 리스트(visit_node)를 출력한다




맨 처음에 while과 for문을 사용해 dfs를 구현하려다가 생각해보니 노드를 옮겨다녀야하기 때문에 while과 for문으로 만들자니 메모리 낭비와 반복 낭비가 예상이 되어 재귀함수로 구현하자 생각
"""
#a는 정점, b는 간선, start는 시작할 정점을 의미
from collections import deque 
a,b,start = list(map(int, input().split()))

#인접행렬 생성. 일단 모두 0으로 값을 넣음.
#생각해보니 문제에 1,4 이렇게 넣는데 실제로 인덱스는 0부터 시작하니 a+1하기
near_node = [ [0]*(a+1) for i in range(a+1)]

#연결되어 있는 노드이면 인접행렬에 1이라고 표시
for _ in range(b):
    i,j = map(int, input().split())
    near_node[i][j] = near_node[j][i] = 1

#방문확인 리스트
dfs_visit_node = [0] * (a+1)
dfs_visit_list = [start]

bfs_visit_node = [0] * (a+1)
bfs_visit_list = [start]

#bfs의 큐
bfs_deque = deque()

def dfs(start):

    #실패코드
    #이거 노드를 옮겨다녀야하는데 즉, x나 y의 좌표를 이동해야하는데 ㄹㅇ 재귀밖에 답이 없을듯?
    # while start <= a:
    #     for i in range(1, a+1):
    #         if i not in dfs_visit_node and near_node[start][i] == 1:
    #             dfs_visit_node.append(i)
    #             print(f"visit_node : {dfs_visit_node}")
    #     start += 1
    # print(dfs_visit_node)

    #방문했으면 1로 만듬
    dfs_visit_node[start] = 1
    for i in range(1, a+1):
        if (dfs_visit_node[i] == 0 and near_node[start][i] == 1):
            dfs_visit_list.append(i)
            dfs(i) #재귀돌림


def bfs(start):
    bfs_visit_node[start] = 1
    bfs_deque.append(start)
    while len(bfs_deque) > 0:
        #현재 위치
        loc = bfs_deque.popleft()
        for i in range(1, a+1):
            if (bfs_visit_node[i] == 0 and near_node[loc][i] == 1):
                bfs_visit_node[i] = 1
                bfs_visit_list.append(i)
                bfs_deque.append(i)

dfs(start)
print(*dfs_visit_list)
bfs(start)
print(*bfs_visit_list)