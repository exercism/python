def find_minimum_coins(total_change, coins):
    if total_change < 0:
        raise ValueError("cannot find negative change values")
    min_coins_required = [1e9] * (total_change + 1)
    last_coin = [0]*(total_change + 1)
    min_coins_required[0] = 0
    last_coin[0] = -1
    for change in range(1, total_change + 1):
        final_result = min_coins_required[change]
        for coin in coins:
            if coin <= change:
                result = min_coins_required[change - coin] + 1
                if result < final_result:
                    final_result = result
                    last_coin[change] = change - coin
        min_coins_required[change] = final_result
    if min_coins_required[total_change] == 1e9:
        raise ValueError("no combination can add up to target")
    else:
        last_coin_value = total_change
        array = []
        while(last_coin[last_coin_value] != -1):
            array.append(last_coin_value-last_coin[last_coin_value])
            last_coin_value = last_coin[last_coin_value]
        return array
