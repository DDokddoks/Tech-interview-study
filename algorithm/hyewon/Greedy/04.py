n = int(input())
coins = list(map(int, input().split()))
coins.sort()
value = 1
for c in coins:
    if value < c:
        break
    value += c
print(value)