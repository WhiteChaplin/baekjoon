#https://www.acmicpc.net/problem/10250
"""
호텔은 직사각형이며 1 <= width <= height <= 99 이다.
엘리베이터는 가장 왼쪽에 있으며 엘리베이터부터 오른쪽으로 101호 102호... 이렇게 방이 존재한다.
방 번호는 YXX 혹은 YYXX인데 Y는 층수 X는 몇번째 방 번호인지 나타낸다.
손님은 무조건 위치가 멀지 않는 방을 선호한다. 단, 엘리베이터를 타고 이동하는 것은 거리에 포함하지 않는다.
예를 들면 101호를 가는데 이동하는 거리는 1, 102호를 가는데 이동하는 거리는 2이다.
단, 엘리베이터를 타고 이동하는것은 이동거리에 포함하지 않기 때문에 102호가 201호보다 멀다. 즉, 102호 보단 201호를 선호한다.
손님 수를 입력받고, 호텔이 몇층 몇번째 호 까지 있는지, 또한 손님이 몇번째 손님인지를 입력받아
손님이 가장 원하는 방의 호실을 출력하라.

알고리즘 설명
 일단 visit_count가 현재 호텔의 방 총 갯수보다 작으면 -1을 반환
 손님은 무조건 거리가 짧은 방을 원하니 1순위는 무조건 위층의 방을 선호함
그래서 일단 위로 올림. 근데 손님 번호가 호텔의 층수보다 많으면 방을 옆으로 1개씩 옮겨야함
그래서 층수를 손님번호 // 높이 로 하고 1층부터 시작해서 +1을 해야함
방 번호는 손님번호 % 높이를 하면 방 번호가 나옴
 만약 손님번호가 호텔 층수보다 작으면 그냥 호텔층수의 1번방을 주면됨

층수, 방수, 손님번호
"""
input_num = int(input())
input_hotel_info_and_visiter_info = []
for i in range(input_num):
    input_hotel_info_and_visiter_info.append(list(map(int, input().split())))

for i in input_hotel_info_and_visiter_info:
    if i[2] > i[0]*i[1]:
        print("-1")
        continue
    elif i[2] % i[0] == 0:
        room_height = str(i[0])
        room_weight = str((i[2] // i[0]))
    elif i[2] // i[0] > 0:
        room_weight = str((i[2] // i[0]) + 1)
        #room_height = i[2] % i[0]
        room_height = str(i[2] % i[0])
    else:
        room_weight = str(1)
        room_height = str(i[2])
    room_weight = room_weight.zfill(2)
    print(room_height+room_weight)
    
