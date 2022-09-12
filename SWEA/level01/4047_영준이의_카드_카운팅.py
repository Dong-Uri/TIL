T = int(input())
for t in range(1, T+1):
    # S, D, H, C을 키로 갖고 출력할 값과 카드가 겹치는지 확인할 값의 리스트를 값으로 가지는 딕셔너리
    card_dict = {'S':[13] + [0] * 13, 'D':[13] + [0] * 13, 'H':[13] + [0] * 13, 'C':[13] + [0] * 13}
    card = input()
    for i in range(0, len(card), 3):

        # 카드가 겹치지 않는다면 체크하고 부족한 카드수 -1
        if card_dict[card[i]][int(card[i + 1:i + 3])] == 0:
            card_dict[card[i]][int(card[i + 1:i + 3])] = 1
            card_dict[card[i]][0] -= 1
            
        # 카드가 겹치면 ERROR
        else:
            print(f'#{t} ERROR')
            break
            
    # ERROR없이 끝난 경우 출력
    else:
        print(f'#{t} {card_dict["S"][0]} {card_dict["D"][0]} {card_dict["H"][0]} {card_dict["C"][0]}')