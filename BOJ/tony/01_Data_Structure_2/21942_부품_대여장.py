import sys
N, L, F = sys.stdin.readline().rstrip().split()
N = int(N)
D_due = int(L[:3])
H_due = int(L[4:6])
M_due = int(L[7:])
F = int(F)
H_due += D_due * 24
M_due += H_due * 60
book_borrow = dict()
book_pay = dict()
M_lst = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
for _ in range(N):
    date, time, part, nick = sys.stdin.readline().rstrip().split()
    MM = int(date[5:7])
    dd = int(date[8:])
    hh = int(time[:2])
    mm = int(time[3:])
    dd += M_lst[MM]
    hh += (dd-1) * 24
    mm += hh * 60
    if part+' '+nick not in book_borrow.keys() or book_borrow[part+' '+nick] == -1:
        book_borrow[part+' '+nick] = mm
    else:
        M_borrow = mm - book_borrow[part+' '+nick]
        if M_borrow > M_due:
            if nick in book_pay.keys():
                book_pay[nick] += (M_borrow - M_due) * F
            else:
                book_pay[nick] = (M_borrow - M_due) * F
        book_borrow[part+' '+nick] = -1
if not book_pay:
    print(-1)
else:
    ans = sorted(book_pay.items(), key=lambda x: x[0])
    for a, b in ans:
        print(a, b)
