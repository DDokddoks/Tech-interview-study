from itertools import combinations
n, m = map(int, input().split())
balls = list(map(int, input().split()))
res = 0

for ball_set in list(combinations(balls, 2)):
    a, b = ball_set
    if a != b:
        res += 1

print(res)