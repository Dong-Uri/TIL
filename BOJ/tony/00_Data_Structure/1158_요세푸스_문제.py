N, K = map(int, input().split())
lst = [n+1 for n in range(N)]
remv = K-1 # 처음 제거될 인덱스
yosep = []
while lst:
    remv %= len(lst)                # 인덱스가 리스트를 넘으면 반복
    yosep.append(str(lst[remv]))    # 제거된 번호를 다른 리스트에 저장
    lst.remove(lst[remv])           # 리스트에서 제거
    remv += K-1                     # remove 때문에 하나 덜 증가
print('<' + ', '.join(yosep) + '>')

# 하위 문제
# 11866_요세푸스_문제_0