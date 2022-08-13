#https://www.acmicpc.net/problem/1712
"""
손익분기점이 넘지 않는 경우는
가변비용이 판매가격보다 높은 경우밖에 없음.

손익분기점은 판매비용의 총이 그동안 제작한 비용의 총계를 넘기면 손익분기점이다.
즉 (상품가격 x 판매대수) <= (고정비용 + 가변비용*판매대수) 를 하면 된다.
"""
a = list(map(int,input().split()))
fix_money = a[0] #고정비용
make_product_price = a[1] #가변비용
product_price = a[2] #판매가격
product_count = 0


#처음에 짠 코드. 시간이 너무 오래걸림
"""
while product_price*product_count <= (fix_money)+(make_product_price*product_count):
    if make_product_price > product_price:
        print(-1)
        break
    is_while = True
    product_count += 1
    sum = fix_money+(make_product_price*product_count)
    #print(sum)
    #print(product_price*product_count)
    if product_price*product_count > sum:
        print(product_count)
        break
"""

if make_product_price >= product_price:
        print(-1)
else:
    product_count = int(fix_money / (product_price - make_product_price))+1
    print(product_count)
