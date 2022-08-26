#https://www.acmicpc.net/problem/2750
"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
버블 정렬 사용
전형적인 버블정렬 사용법이다.
버블정렬 알고리즘
맨 앞 인덱스부터 뒤로 이동하면서 n과 n+1번 인덱스끼리 비교하면서 정렬하는 방식이다.
한 사이클을 돌리면 제일 높은 숫자가 맨 뒤로 간다. 그래서 한 사이클에서 실행되는 반복은
사이클이 늘어남에 따라 1씩 감소한다.
1. 전체 반복 횟수는 len(array)-1로 설정한다.
2. 한 사이클을 진행한 반복은 len(array)-i-1로 설정한다.
3. n번 인덱스와 n+1 인덱스끼리 비교한다.
4. 만약 n+1번 인덱스가 n보다 작다면 둘의 값을 변경한다.
5. 마지막 인덱스 번까지 반복하면 한 사이클이 끝난다.
6. 이 사이클을 len번 반복하면 된다.
"""

input_num = int(input())
num_list = []
for i in range(input_num):
    num_list.append(int(input()))

for i in range(input_num-1):
    for j in range(input_num-i-1):
        if num_list[j] > num_list[j+1]:
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = temp
        
for i in num_list:
    print(i)