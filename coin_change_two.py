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


# def recursiveChange():








if __name__ =="__main__":
    denominations =[7]
    target = 9
    print(coinChange(denominations, target))