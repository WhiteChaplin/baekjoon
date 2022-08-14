#https://www.acmicpc.net/problem/2798
"""
N개의 카드 중 3장을 골라 맞춰야 하는 수에 제일 가깝게 하면 된다.
즉, 배열에서 3개의 수를 뽑아 맞춰야 하는 수에 제일 가깝게 하면 된다.
M을 넘지 않는 3개의 합을 출력하면 된다.
3 <= N <= 100   3 <= M <= 300,000
실패한 알고리즘들을 적어놓았다. 생각을 엄청 해보았으나 결국에는
전수조사밖에 풀이가 없다고 생각하여 전수조사로 진행한다.
3개의 카드를 조합하는 방식이라 편하게 작성하면
1 2 3 인덱스, 1 2 4 인덱스 1 2 5 인덱스... 이렇게 한개씩 늘려가면서
카드의 값의 합을 조합하여 원하는 값을 넘지 않는 가장 가까운 값을
찾으면 된다.
"""
import time
card_count, want_number = map(int,input().split())
card_list = list(map(int,input().split()))
card_list = card_list[:card_count]
card_list.sort()
end_index = len(card_list)
sum_num = 0
sum_num_max = 0
"""
실패한 알고리즘
이유: 일단 리스트를 순차대로 정렬한다.
      원하는 수를 3으로 나누고 그 나눈값 혹은 근처의 값의 인덱스를 찾아
      기준 인덱스의 0 -1 -2번째 인덱스를 더하거나 만약 값이 원하는 수를 넘어가면
      -1 -2 -3번 인덱스를 더한다.
      평균값으로 접근한 방식인데 잘못된 이유는 블랙잭은 원하는 수 근처로 가야하기
      때문에 무조건 근접한 값이 나와야 한다. 즉, 전수조사를 해서라도 근처의 값의
      조합을 찾아야 한다. 잘못된 접근 방식이었다.
if want_number // 3 in card_list:
    print(f"card_list: {card_list.index(want_number // 3)}")
else:
    middle_index = [ index for index,x in enumerate(card_list) if x > want_number // 3]
    print(f"middle_index: {min(middle_index)}")
    
    if min(middle_index) < 2:
        print("불가능함")
    elif min(middle_index) == 2 :
        sum_num = card_list[:3]
        if sum(sum_num) > want_number:
            print("불가능함")
        else:
            print(sum(sum_num))
    else:
        sum_num =  card_list[middle_index[0]:middle_index[0]-3:-1]
        if sum(sum_num) > want_number :
            sum_num = sum_num =  card_list[middle_index[0]-1:middle_index[0]-4:-1]
            print(sum(sum_num))
        else:
            print(sum(sum_num))
"""

"""
실패한 알고리즘
이유: 전수조사를 해야한다고 생각하였으나 전수조사의 방식이 잘못되었다.
      0번 인덱스와 마지막 인덱스를 더하고, 중간의 수를 인덱스를 하나씩 올리면서
      더하는 방식을 생각했다. 즉 0번인덱스, 마지막 인덱스를 더하고 1번,2번,3번
      한개씩 더하면서 수를 다 더해보는 방식이고,
      사이클이 끝나면 시작 인덱스를 하나 올리고 사이클 돌리고,
      마지막 인덱스를 하나 내리고 사이클 돌리는 방식으로
      0 10, 1 10, 1 9, 2 9, 2 8 이렇게 사이를 좁히는 방식을 사용하였다.
      하지만 이렇게 하면 3 6 이런 인덱스가 불가능하다는걸 깨닿게 되었다.
      실행시간을 줄이기 위해 고안해낸 방식이었으나 완전히 잘못되었다.
is_start = True
is_end = False
start = time.time()
while end_index - start_index != 1:
    for i in card_list[start_index+1:end_index]:
        sum_num = card_list[start_index] + card_list[end_index-1] + i
        if sum_num > want_number:
            continue
        elif sum_num > sum_num_max:
            sum_num_max = sum_num
        elif sum_num == want_number:
            sum_num_max = sum_num
            break
    if is_start:
        start_index += 1
        is_start = not is_start
    else:
        is_start = not is_start
    if is_end:
        end_index -= 1
        is_end = not is_end
    else:
        is_end = not is_end
    print(f"start: {start_index}, end: {end_index}")

print(time.time() - start)
print(sum_num_max)
"""

#전수계산 다 때려보자 index[1]+index[2]+index[3] , index[1]+index[2]+index[4]
for i in range(end_index):
    for j in range(i+1,end_index):
        for k in range(j+1, end_index):
            if card_list[i]+card_list[j]+card_list[k] > want_number:
                continue
            else:
                #sum_num_max = max(sum_num_max, card_list[i]+card_list[j]+card_list[k])
                sum_num = card_list[i]+card_list[j]+card_list[k]
                if sum_num > sum_num_max:
                    sum_num_max = sum_num

print(sum_num_max)



