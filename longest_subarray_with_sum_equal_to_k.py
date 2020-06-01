" Kardane's algorithm "

def longest_subarray(nums,target: int) -> int:
    prevSum ={0:-1}
    carrSum =0
    result =0
    for i,k  in enumerate(nums):
        carrSum += k
        if carrSum - target in prevSum:
            if result < (i - prevSum[carrSum - target]):
                result = i - prevSum[carrSum - target]
        if carrSum not in prevSum:
            prevSum[carrSum] = i
    return result

if __name__ =="__main__":
    nums =[10, 5, 7, 1, 2, 5, 3]
    target = 15
    print(longest_subarray(nums, target))

