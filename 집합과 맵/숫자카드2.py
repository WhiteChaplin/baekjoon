#https://www.acmicpc.net/problem/10816
"""
list comprehension으로 시간초과가 나오니 다른 방법을 찾아야지
collecion 모듈의 conuter 함수가 있다. 시퀀스 자료형의 요소의 갯수를 dict 자료형으로 만들어 바꿔준다.

알고리즘 설명
1. my_card_list를 Counter함수를 이용해 어떤 숫자가 몇개 들어있는지 dict으로 만든다.
2. list comprehension로 비교할 카드 리스트인 card_list의 요소를 dict의 key값으로 이용해 몇개가 들어있는지 확인한다.
   만약 card_list에 요소가 my_card_list에 없다면 0을 넣는다.
3. 최종적으로 들어가 있는 리스트를 unpacking하여 출력한다.

comprehension보다 내장되어 있는 기본 함수를 사용하는 것이 더 빠르구나....
"""
from collections import Counter
import sys
my_card_count = sys.stdin.readline()
my_card_list = sys.stdin.readline().split()
card_list_num = sys.stdin.readline()
card_list = sys.stdin.readline().split()

my_card_list_Counter = Counter(my_card_list)
result = [my_card_list_Counter[index] if index in my_card_list_Counter else 0 for index in card_list]
print(*result)