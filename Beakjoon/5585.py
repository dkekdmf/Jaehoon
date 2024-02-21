def greedy(change, coin_list):
    counts = {}
    for coin in sorted(coin_list,reverse=True):
        coin_count = change//coin
        if coin_count>0:
            counts[coin]= coin_count
            change -= coin*coin_count
    result = []
    for coin,count in counts.items():
            result.append(f"{coin}*{count}")
    return f"{sum(counts.values())}"
change = int(input())
coin_list1 = [2,5]
print(greedy(change, coin_list1))  
