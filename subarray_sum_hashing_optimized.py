from collections import defaultdict
def findSubarray(arr, n, sum):
    prevSum = defaultdict(lambda : 0)
    res = 0
    currsum = 0
    for i in range(0, n):
        currsum += arr[i]
        if currsum == sum:
            res += 1
        if currsum - sum in prevSum:
            print(arr[i], i )
            res += prevSum[currsum - sum]
            print(prevSum)
        prevSum[currsum] += 1
    print(prevSum)
    return res


if __name__ == "__main__":
    arr =[3,6,-10,7,10,3,1,2]
    sum = 3
    n = len(arr)
    print(findSubarray(arr, n, sum))


