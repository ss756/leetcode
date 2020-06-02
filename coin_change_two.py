def coinChange(nums,amount: int) -> int:
    arr = [float('inf') for _ in range(0,amount+1)]
    arr[0] = 0
    for value in nums:
        for j in range(1, amount+1):
            if j >= value:
                if arr[j] > arr[j-value]:
                    arr[j] = arr[j - value]+1
    print(arr)
    if arr[amount] != float('inf'):
        return arr[amount]
    else:
        return -1


def count(S, m, n):
    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0 for k in range(n + 1)]

    # Base case (If given value is 0)
    table[0] = 1

    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0, m):
        for j in range(S[i], n + 1):
            table[j] += table[j - S[i]]

    return table[n]







if __name__ =="__main__":
    denominations =[1,2,5]
    target = 5
    #print(coinChange(denominations, target))
    print(count(denominations, len(denominations),target))