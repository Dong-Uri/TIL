for t in range(1, 11):
    N = int(input())
    crypt = list(input().split())
    M = int(input())
    order = list(input().split())
    
    # 명령 수행
    for i in order:
        
        # 명령의 기능을 받는 경우
        if i == 'I':
            mode = 'Ix'
        elif i == 'D':
            mode = 'Dx'
        elif i == 'A':
            mode = 'Ay'
            
        # 삽입 명령을 받은 경우
        elif mode == 'Ix':
            Ix = int(i)
            mode = 'Iy'
        elif mode == 'Iy':
            Iy = int(i)
            crypt = crypt[:Ix] + [0] * Iy + crypt[Ix:] # 일단 0을 삽입
            cnt = 0
            mode = 'Is'
        elif mode == 'Is':
            crypt[Ix + cnt] = i # 미리 삽입된 0을 고쳐나감
            cnt += 1
            
        # 삭제 명령을 받은 경우
        elif mode == 'Dx':
            Dx = int(i)
            mode = 'Dy'
        elif mode == 'Dy':
            Dy = int(i)
            crypt = crypt[:Dx] + crypt[Dx + Dy:] # 삭제
            
        # 추가 명령을 받은 경우
        elif mode == 'Ay':
            mode = 'As'
        elif mode == 'As':
            crypt += [i] # 추가
            
    print(f'#{t}', *crypt[:10])