# 3달 이용권을 사용할지 계산해보는 함수
def plan_3M(i, bill):
    global min_price
    if i >= 12:
        if bill < min_price:
            min_price = bill
        return
    
    # 3달 이용권이 이득인 경우 사용하는 계산
    if month_min[i] and sum(month_min[i:i+3]) > price[2]:
        plan_3M(i + 3, bill - sum(month_min[i:i+3]) + price[2])

    # 3달 이용권을 사용 안하는 계산
    plan_3M(i + 1, bill)

T = int(input())
for t in range(1, T+1):
    price = list(map(int, input().split()))
    schedule = list(map(int, input().split()))
    min_price = price[3]    # 연간 이용권 사용을 최소 비용 기준으로 함
    month_min = []
    for s in schedule:      # 1일 이용권 사용과 1달 이용권 사용중 이득인 것을 한달 비용 기준으로 함
        month_min.append(min(price[1], price[0] * s))
    plan_3M(0, sum(month_min))
    print(f'#{t} {min_price}')