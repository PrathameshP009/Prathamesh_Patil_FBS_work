n = int(input("Enter total number of coins: "))
coins = list(map(int, input("Enter coin numbers: ").split()))

missing = 0
for coin in coins:
    missing ^= coin

print("Missing coin number is:", missing)
