from itertools import permutations

fil = input()

try:
    file = open(fil).readlines()
except:
    print("File Tidak Ada")
    exit()

n = int(file[0])
games = []
for i in range(1, n + 1):
    belah = file[i].split()
    a = int(belah[0])
    b = int(belah[1])
    games.append((a, b))

beats = {'H': 'S', 'S': 'P', 'P': 'H'}
moves = ['H', 'P', 'S']

max_menang = 0

for perm in permutations(moves):
    mapping = {1: perm[0], 2: perm[1], 3: perm[2]}
    menang = 0
    for a, b in games:
        if beats[mapping[a]] == mapping[b]:
            menang += 1
    if menang > max_menang:
        max_menang = menang

print(max_menang)