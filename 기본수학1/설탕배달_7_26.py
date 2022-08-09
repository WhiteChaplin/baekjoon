#https://www.acmicpc.net/problem/2839
"""
설탕공장에서 설탕을 배달하는데 설탕포대는 3kg와 5kg 2개밖에 없다
이 2개를 이용해 배달할 설탕의 총 포대 수를 가장 적게 만드는 것이 목표
만약 원하는 무게의 설탕이 배달이 안되면 -1 반환
주의!
3kg을 어떻게 처리할지가 매우 중요함. 일반적으로 짰다가 3kg가 놀고 있어서 다시 짰음
나는 3kg을 총 12kg까지 빼보고 만약 3kg씩 빼다가 5의 배수의 수가 나오면 그 즉시 5kg으로 나누는 방식을 사용했음
왠만한 수가 12kg안에 3kg를 처리할 수 있기 때문 12kg한 이유는 15kg가 3와 5의 배수이기 때문에 그 전인 12를 선택함
"""
trans_suger = int(input())
suger_box_5kg = 0
suger_box_3kg = 0


for i in range(4):
    if trans_suger % 5 == 0:
        suger_box_5kg = trans_suger // 5
        break
    else:
        trans_suger -= 3
        suger_box_3kg += 1

        
if trans_suger < 0:
    print("-1")
else:
    if trans_suger % 5 == 0:
        suger_box_5kg = trans_suger // 5
        print(int(suger_box_3kg+suger_box_5kg))
    else:
        print("-1")