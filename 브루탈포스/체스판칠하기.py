#https://www.acmicpc.net/problem/1018
"""
정답을 보면서 코딩함.
다 보진 않고 슬라이싱 부분이 애매해서 5시간정도 고민하고 코딩하다 안돼서 정답봄
배열 슬라이싱에 조금 더 공부를 해야할듯
2차원 배열과 배열 슬라이싱에 대해 더 알아야겠음.
조금 더 쉽게 코딩을 할 수 있는 방법이라 해설을 보는거도 좋은 공부법인 듯 함.

알고리즘 설명
체스 판 배열은 2가지가 있다.
1. 2줄 기준 시작이 흰색, 다음줄 마지막이 흰색인 경우
2. 2줄 기준 시작이 검은색, 다음줄 마지막이 검은색인 경우

입력받은 체스판을 8 x 8 배열로 슬라이싱하고
2줄별로 기존 체스판 배열과 비교하여
만약 틀린 색이 있다면 카운트를 올리고
슬라이싱된 8 x 8 배열 중 가장 카운트가 낮은 것을 고른다.

결론적으로 for문을 4번 쓰는 것 까지는 맞았으나
배열을 자르는 부분에서 애를 먹었던 거 같음.
"""
chess_color1 = "WBWBWBWBBWBWBWBW"
chess_color2 = "BWBWBWBWWBWBWBWB"

a,b = map(int,input().split())

chess_state = []
for i in range(a):
    chess_state.append(input())

#chess_state = list(chess_state.split(" ")) #입력한 체스판을 공백을 기준으로 나눔
print(chess_state)
min = 64
count_color1 = 0
count_color2 = 0


for row in range(a-7): #만약 row가 10이라면 총 반복은 8 9 10. 총 3번을 해야하기 때문에 7을 빼준다.
    for column in range(b-7): #만약 row가 11이라면 총 반복은 8 9 10 11. 총 4번을 해야하기 때문에 7을 빼준다
        count_color1 = 0 #chess_color1과 비교했을 때 아닌 부분 카운트
        count_color2 = 0 #chess_color2와 비교했을 때 아닌 부분 카운트
        select_pos = "" #chess_color와 비교하는 문자열. 기존 배열을 슬라이싱해서 넣음

        #여기서부터는 자른 배열을 담고 입력된 배열과 비교하는 코드 8 x 8로 자를 것임
        for inner_row in chess_state[row:row+8]: #입력 받은 체스판에서 자를 부분의 열을 지정함
            select_pos += inner_row[column:column+8] #select_pos에 현재 자를 부분의 열의 행을 넣음
            if len(select_pos) == 16: #chess_color1과 2가 16개이고 체스판 색칠 규칙이 2줄(16개)의 색 순서이기 때문에 16개씩 비교
                #print(select_pos)
                for i in range(16):
                    if select_pos[i] != chess_color1[i]:
                        count_color1 += 1
                    elif select_pos[i] != chess_color2[i]:
                        count_color2 += 1
                select_pos = "" #다음 2줄로 넘어감

        if count_color1 <= count_color2 and count_color1 < min :
            min = count_color1
        elif count_color2 < count_color1 and count_color2 < min :
            min = count_color2

print(min)
 

