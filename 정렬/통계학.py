#https://www.acmicpc.net/problem/2108
"""
N개의 수를 입력받아 통계처리를 진행한다. 단 N은 홀수라고 가정한다
1. 산술평균: N개의 수들의 합을 N으로 나눈 값. 소수점 이하 첫째 자리에서 반올림
2. 중앙값: N개의 수를 증가하는 순서로 나열 시 중앙에 위치하는 값
3. 최빈값: N개의 수 중에서 가장 많이 나타나는 값. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
4. 범위: N개의 수들 중 최대값과 최빈값의 차이
"""
import math
import sys
from collections import Counter
#개어이없네. 계속 시간에러 나길래 왜이러나 싶어서 코드 다 엎어보고 안되겠다 싶어서
#구글 뒤져보니 입력을 sys.stdin.readline()으로 받으라더라. 이게 시간초과에러 안난다고
num = int(sys.stdin.readline())
num_list = []
for _ in range(num):
    num_list.append(int(sys.stdin.readline()))

#평균
mean = round(sum(num_list)/num)

#중앙값
num_list.sort()
index = len(num_list)//2
middle = num_list[index] 


#최빈값 출력. 만약 여러개일 시 2번째로 작은 값 출력
#수업시간에 배운 collections모듈의 Counter함수를 이용하자
#counter함수는 시퀀스 자료형의 데이터의 값의 개수를 dictionary 형태로 변환한다
repeat_dict = Counter(num_list)
most = repeat_dict.most_common()
repeat = 0

#조건에 대한 값이 너무 많아 for문 돌리면 안될 거 같다.
if len(most) == 1:
    repeat = most[0][0]
else:
    if most[0][1] == most[1][1]:
        repeat = most[1][0]
    else:
        repeat = most[0][0]

#틀렸다고 나오는데 왜 틀린건지 모르겠음...뭔가 for문 쓰면 안될 거 같아서 지움. 조금 생각을 해봐야할듯
# count_num = 0
# max_repeat_str_list = []
# max_repeat_count_num = 0
# set_list = list(set(num_list))
# set_list.sort()
# for i in set_list:
#     count_num = num_list.count(i)
#     if len(set_list) == 1:
#         print(set_list[0])
#         break
#     elif count_num > max_repeat_count_num:
#         max_repeat_str_list = []
#         max_repeat_count_num = count_num
#         max_repeat_str_list.append(i)
#     elif count_num == max_repeat_count_num:
#         max_repeat_str_list.append(i)
#         if len(max_repeat_str_list) == 2:
#             print(max_repeat_str_list[1])
#             break;





print(mean)
print(middle)
print(repeat)
print(max(num_list) - min(num_list)) #범위