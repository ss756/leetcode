import sys
def coin_change(denominations, target:int):
    n = len(denominations)
    arr = list()
    arr = [float('inf') for _ in range(0,target+1)]
    arr[0] = 0
    print(arr)
    for i in range(0,len(denominations)):
        for j in range(1, target+1):
            if j >= denominations[i]:
                if arr[j] > arr[j-denominations[i]]:
                    arr[j] = arr[j - denominations[i]]+1
    print(arr)
    if arr[target] != float('inf'):
        # Accept, return total count of coin change
        return arr[target]
    else:
        # Reject, no solution
        return -1


def coinChange( coins, amount: int) -> int:

        # initialization for dp_table
        dp_table = [float('inf') for _ in range(amount + 1)]

        # base case for $0
        dp_table[0] = 0

        for value in range(1, amount + 1):
            for coin in coins:
                if coin > value:
                    # coin value is to big, can not make change with current coin
                    continue

                # update dp_table, try to make change with coin
                dp_table[value] = min((dp_table[value], dp_table[value - coin] + 1))

        if dp_table[amount] != float('inf'):
            # Accept, return total count of coin change
            return dp_table[amount]
        else:
            # Reject, no solution
            return -1

if __name__ == "__main__":
    l = [7]
    target = 6
    print (coin_change(l,target))
    print((coinChange(l,target)))
