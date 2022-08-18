#https://www.acmicpc.net/problem/2231
"""
어떤 자연수 N이 있을 시 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
예를 들면 245의 분해합은 256(=245+2+4+5)가 된다.
따라서 245는 256의 생성자가 된다. 물론 생성자가 없을 수도 있다.
반대로, 생성자가 여러개인 자연수도 있을 수 있다.
자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구하는 프로그램을 작성하라

알고리즘 설명
계속 숫자를 지긋이 쳐다보니 특정 숫자에서는 규칙이 생겼다.
1. 3의배수
  3의배수는 무조건 생성자가 3의배수 규칙 때문에 생성자 역시 3의 배수이다.
2. 9의배수
  9의배수 역시 무조건 생성자가 9의 배수이다. 
3. 1과2에 조건에 해당하지 않는 경우는 어쩔 수 없이 for문을 이용해
    입력받은 값에서 1씩 빼면서 생성자를 찾는 방법밖에 없는 거 같다.
    하지만 for문을 무작정 돌리지 않고 조건에 맞춰 돌리는데
    최대한으로 for문을 반복하는 횟수는 최대 (입력받은 숫자의 자리수-1) x 9이다
    1026 -> 999, 117 -> 99 를 보면서 찾은 규칙인데
    생성자를 만들 수 있는 가장 최소 조건이 (자리수-1) x 9 이기 때문이며
    이보다 낮은 숫자는 입력받은 숫자의 생성자가 될 수 없다.
    반례의 조건을 찾았다. 29인데 29의 생성자는 19로 10번을 반복해야 해서 (입력받은 숫자의 자리수 -1) x 9의 조건을 깨트린다.
    그래서 조금 널널하게 (자리수-1) x 9 로 진행한다.
    그리고 또한 반복하면서 숫자가 마이너스로 가는 것을 방지해주어야 한다.
이를 활용하여 알고리즘을 짜면 된다.
"""
import math
input_num = int(input())
make_num = 0
if input_num < 0:
    pass
else:
    num_digit = int(math.log10(input_num)) + 1

if input_num % 9 == 0:
    input_num_temp = input_num
    for i in range(0,((num_digit)*9)+1,9):
        input_num_temp -= 9
        if input_num_temp < 0 :
            break
        elif input_num == input_num_temp + sum(map(int, str(input_num_temp))):
             make_num = input_num_temp
elif input_num % 3 == 0:
    input_num_temp = input_num
    for i in range(0,((num_digit)*9)+1,3):
        input_num_temp -= 3
        if input_num_temp < 0 :
            break
        elif input_num == input_num_temp + sum(map(int, str(input_num_temp))):
             make_num = input_num_temp
else:
    input_num_temp = input_num
    for i in range(0, ((num_digit)*9)+1):
        input_num_temp -= 1
        if input_num_temp < 0 :
            break
        elif input_num == input_num_temp + sum(map(int, str(input_num_temp))):
            make_num = input_num_temp

print(f"make_num : {make_num}")

