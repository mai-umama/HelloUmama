A, B = map(int, input().split())

coin = max(2*A - 1, 2*B - 1, A + B)

print(coin)
