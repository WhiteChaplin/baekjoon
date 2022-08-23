#https://www.acmicpc.net/problem/7568
"""
n개의 인원의 몸무게와 키를 입력받고
만약 자신의 몸무게와 키가 다른 사람의 몸무게와 키보다 크다면
내가 더 덩치가 큰 것으로 계산한다.

알고리즘 설명
1. 받은 값들을 리스트의 2차원 배열로 저장한다.
2. 기준 값을 설정한다. 기준 값은 한명씩 돌아가면서 해야하기 때문에
   for문을 리스트의 길이로 설정한다.
   기준 값은 받은 리스트에서 맨 앞에 값을 pop을 해서 빼낸다.
3. 기준값과 기준값이 빠진 기존 리스트의 값들을 처음부터 하나씩 비교한다.
   만약 기준값과 리스트에서 빼온 값끼리 서로 비교했을 때
   키와 몸무게가 빼온 값이 더 작으면 count+=1을 한다
4. 한 사이클이 종료되면 big_list라는 count의 값을 담는 리스트에
   count 값을 추가한다. 이것은 나중에 등수를 지정하는 리스트로 이용한다.
5. 모든 사이클이 종료되면 이제 등수를 설정해야한다.
   big_list의 값을 하나씩 비교한다. big_list[0]과 big_list[0], big_list[0]과 big_list[1] ....
6. 만약 big_list[i] > big_list[j] 라면 자신의 덩치가 더 작은것이니 rank += 1을 하면 된다.
7. 최종적으로 rank가 담긴 list를 반환하면 된다.
"""

people_num = int(input())
people_info_list = []
big_list = []
for i in range(people_num):
    a = list(map(int,input().split(" ")))
    people_info_list.append(list(a))

#1개의 기준 리스트와, 나머지 리스트들의 원소를 다 꺼냄
for i in range(people_num):
    temp = people_info_list.pop(0)
    count = 1
    for k in range(len(people_info_list)):
        if temp[0] < people_info_list[k][0] and temp[1] < people_info_list[k][1]:
            count+=1
    people_info_list.append(temp)
    big_list.append(count)


print(*big_list)
