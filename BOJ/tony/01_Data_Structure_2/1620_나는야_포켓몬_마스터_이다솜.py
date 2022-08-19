import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
pokedex = [0] * (N + 1)
pokedict = {}
for n in range(1, N+1):
    poke = sys.stdin.readline().rstrip()
    pokedex[n] = poke
    pokedict[poke] = n
for _ in range(M):
    quiz = sys.stdin.readline().rstrip()
    if 48 <= ord(quiz[0]) <= 57:
        print(pokedex[int(quiz)])
    else:
        print(pokedict[quiz])