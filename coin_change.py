import sys
# def coin_change(denominations, target:int):
#     arr = [None]*(target+1)
#     n = len(denominations)
#     arr[0] = 0
#     print(arr)
#     for k in range(1, target+1):
#         arr[k] = sys.maxsize
#     for i in range(0, target):
#         for j in range(1, target+1):
#             if j >= denominations[i]:
#                 if arr[j] > arr[j-denominations[i]]:
#                     arr[j] = arr[j - denominations[i]+1]
#     return arr[target]

# import sys
# def coinChange( nums, amount: int) -> int:
#         coins = list(range(amount+1))
#         if amount == 0:
#             return -1
#         coins[0] = 0
#         for k in range(1, amount + 1):
#             coins[k] == sys.maxsize
#         for i in range(1, amount + 1):
#             for j in range(0, len(nums)):
#                 if nums[j] <= i:
#                     tempcoins = coins[i - nums[j]]
#                     if tempcoins != sys.maxsize and tempcoins + 1 < coins[i]:
#                         coins[i] = tempcoins + 1
#         print(coins[amount])
#         if coins[amount]:
#             return coins[amount]
#         else:
#             return -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

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
    l = [2]
    target = 3
    print (coinChange(l,target))
