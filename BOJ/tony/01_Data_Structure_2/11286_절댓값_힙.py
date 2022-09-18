import sys
N = int(sys.stdin.readline().rstrip())
heap = [0] * 100001
size = 0
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if size == 0:
            print(0)
        else:
            print(heap[1])
            heap[1], heap[size] = heap[size], heap[1]
            size -= 1
            i = 1
            while 2 * i <= size:
                abs_i = abs(heap[i])
                abs_ch1 = abs(heap[2 * i])
                if 2 * i == size:
                    if abs_ch1 < abs_i or (abs_ch1 == abs_i and heap[2 * i] < heap[i]):
                        heap[2 * i], heap[i] = heap[i], heap[2 * i]
                        i = 2 * i
                    else:
                        break
                else:
                    abs_ch2 = abs(heap[2 * i + 1])
                    min_i = min(abs_i, abs_ch1, abs_ch2)
                    if min_i == abs_i:
                        if heap[i] < abs_i:
                            break
                        elif min_i == abs_ch1 and heap[2 * i] < abs_ch1:
                            heap[2 * i], heap[i] = heap[i], heap[2 * i]
                            i = 2 * i
                        elif min_i == abs_ch2 and heap[2 * i + 1] < abs_ch2:
                            heap[2 * i + 1], heap[i] = heap[i], heap[2 * i + 1]
                            i = 2 * i + 1
                        else:
                            break
                    elif min_i == abs_ch1:
                        if abs_ch1 < abs_ch2 or (abs_ch1 == abs_ch2 and heap[2 * i] <= heap[2 * i + 1]):
                            heap[2 * i], heap[i] = heap[i], heap[2 * i]
                            i = 2 * i
                        else:
                            heap[2 * i + 1], heap[i] = heap[i], heap[2 * i + 1]
                            i = 2 * i + 1
                    else:
                        heap[2 * i + 1], heap[i] = heap[i], heap[2 * i + 1]
                        i = 2 * i + 1
    else:
        size += 1
        heap[size] = x
        i = size
        while i // 2:
            abs_i = abs(heap[i])
            abs_pr = abs(heap[i // 2])
            if abs_pr > abs_i or (abs_pr == abs_i and heap[i // 2] > heap[i]):
                heap[i // 2], heap[i] = heap[i], heap[i // 2]
                i //= 2
            else:
                break