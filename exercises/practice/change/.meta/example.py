def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    min_coins_required = [1e9] * (target + 1)
    last_coin = [0] * (target + 1)
    min_coins_required[0] = 0
    last_coin[0] = -1
    for change in range(1, target + 1):
        final_result = min_coins_required[change]
        for coin in coins:
            if coin <= change:
                result = min_coins_required[change - coin] + 1
                if result < final_result:
                    final_result = result
                    last_coin[change] = change - coin
        min_coins_required[change] = final_result
    if min_coins_required[target] == 1e9:
        raise ValueError("can't make target with given coins")
    else:
        last_coin_value = target
        array = []
        while last_coin[last_coin_value] != -1:
            array.append(last_coin_value-last_coin[last_coin_value])
            last_coin_value = last_coin[last_coin_value]
        return array
