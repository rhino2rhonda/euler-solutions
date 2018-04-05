# Problem 31 - Coin Sums

coins = [1,2,5,10,20,50,100,200]
coins.reverse()
mem = { x : { y : None for y in range(201)} for x in coins}

def compute(coin_index, left):
    coin = coins[coin_index]
    # comuted
    if mem[coin][left] is not None:
        return mem[coin][left]
    # smallest coin
    if coin_index >= len(coins) - 1:
        count = 1
    # left < coin
    elif left < coin:
        count = compute(coin_index+1, left)
    # left >= coin
    else:
        count = compute(coin_index+1, left) + compute(coin_index, left-coin)
    mem[coin][left] = count
    return count

print compute(0, 200)

