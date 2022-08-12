#https://www.acmicpc.net/problem/2869
"""
달팽이는 높이가 H미터인 나무 막대를 올라간다.
낮에는 A미터를 올라가고 밤에는 B미터 내려온다. 정상에 올라가면 내려가진 않는다.
나무 막대를 다 올라가려면 몇일이 걸리는지 구하는 코드를 짜시오

알고리즘 설명
일단 높이 - 밤에 내려가는 m를 해준다. 왜냐? 이미 도달했는데 다시 내려가는 불상사를 막기 위해서이다.

1. noon_up - night_down == 1인 경우
    이런 경우 무조건 소요일은 height - night_down이다.
    왜냐? noon_up - night_down == 1이라 무조건 하루에 1씩 증가할 수 밖에 없다.
    계속 1씩 증가하다가 height - night_down인 날에 정상에 도달한다.
    왜냐? height - noon_up인 날은 1이 부족하다. 이미 1이 빠져버렸기 때문이다.

2. (height - night_down) / (noon_up - night_down) == 1 인 경우
    높이가 올라감-내려감로 나눴을 때 1이면 무조건 2일차에 정상에 도달한다.

3. 1,2번의 조건에 맞지 않는다면
    math.ceil()이란 함수가있는데 올림을 하는 메소드이다.
    math.ceil( (height - night_down) / (noon_up - night_down)) 하면 된다.
    소숫점이 나온다는 의미는 그날은 도달하지 못한다는 의미라 올림을 하면 도달하는 날이 나온다,

"""
import math
input_info = list(map(int,input().split()))
tree_height = input_info[2]
noon_up_meter = input_info[0]
night_down_meter = input_info[1]
"""
#첫번째로 짠 코드. 이 코드는 for문으로 짜면 안된다.
#왜냐 조건이 코드 실행 시간이 0.15초 이내여야 한다.
tree-height -= night_down_meter
while now_height < tree_height:
    if noon_up_meter <= night_down_meter:
      print("이러면 못올라갑니다")
      break
    else:
        now_height = now_height + noon_up_meter
        if now_height >= tree_height:
            day_count += 1
            print(f"현재 위치: {now_height}m, day_count = {day_count}")
            break
        else:
            now_height -= night_down_meter
            day_count += 1
            print(f"현재 위치: {now_height}m, day_count = {day_count}")

print(day_count)
"""
#2번째로 짠 코드 for문을 돌리지 않아 실행속도가 빠르다.
if int(tree_height-night_down_meter / (noon_up_meter - night_down_meter)) == 1:
    day_count = 2
elif noon_up_meter - night_down_meter == 1:
    day_count = tree_height - night_down_meter
else:
    day_count = math.ceil( (tree_height-night_down_meter) / ( noon_up_meter - night_down_meter )) 

print(day_count)
