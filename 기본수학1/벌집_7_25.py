#https://www.acmicpc.net/problem/2292
"""
알고리즘 설명
한 사이클의 시작 부분은 1,2,9,22,41,66...이렇게 되어 있는데
이는 1  2  9   22  41  66 ...
      1  7  13   19  25 이렇게 1로 시작하여 자기 자신과 6을 더한 값이
한 사이클의 크기로 이어지고 있다.
근데 만약 1을 빼버리면 6 12 18.. 이렇게 되어서
6*num을 빼면서 진행하겠다.
"""

find_num = int(input())
num = 1
if find_num == 1:
    pass
else:
    while find_num > 1:
        find_num -= (6*num)
        num+=1

print(num)