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
                if 2 * i == size:
                    if heap[2 * i] > heap[i]:
                        heap[2 * i], heap[i] = heap[i], heap[2 * i]
                        break
                    else:
                        break
                else:
                    max_i = max(heap[i], heap[2 * i], heap[2 * i + 1])
                    if max_i == heap[i]:
                        break
                    elif max_i == heap[2 * i]:
                        heap[2 * i], heap[i] = heap[i], heap[2 * i]
                        i = 2 * i
                    else:
                        heap[2 * i + 1], heap[i] = heap[i], heap[2 * i + 1]
                        i = 2 * i + 1
    else:
        size += 1
        heap[size] = x
        i = size
        while i // 2:
            if heap[i // 2] < heap[i]:
                heap[i // 2], heap[i] = heap[i], heap[i // 2]
                i //= 2
            else:
                break