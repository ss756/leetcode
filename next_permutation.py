
class Solution:
    # def critical_point(self, nums):
    #     j = len(nums)-1
    #     while j >0:
    #         if nums[j-1] < nums[j]:
    #             return j-1
    #         j -=1
    #     if j == 0:
    #         return -1
    #
    # def swap(self, nums, index: int):
    #     j = len(nums)-1
    #     print(index)
    #     while nums[index] > nums[j]:
    #         j -=1
    #     temp = nums[j]
    #     nums[j] = nums[index]
    #     nums[index] = temp
    #     reverse = nums[index+1:]
    #     nums = nums[:index+1] + reverse[::-1]
    #     return nums
    #
    #
    # def __init__(self):
    #     nums = [1,2,3]
    #     inverse_point = self.critical_point(nums)
    #     if inverse_point == -1:
    #         print(nums[::-1])
    #     else:
    #         nums = self.swap(nums, inverse_point)
    #         print("final result", nums)


        def nextPermutation(self, nums) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            j = len(nums) - 2
            while j >= 0 and nums[j] >= nums[j + 1]:
                j -= 1
            if j == -1:
                return nums.sort()
            print(j)
            for k in reversed(range(j, len(nums))):
                print(nums[j], nums[k], "check")
                if nums[j] < nums[k]:
                    print("hola", k)
                    nums[j], nums[k] = nums[k], nums[j]
                    break
            nums[j + 1:] = reversed(nums[j + 1:])
            print(nums)
            return nums


        def __init__(self):
            nums = [9, 1, 2, 4, 3, 1, 0]
            nums1= [5, 1, 1]
            print(self.nextPermutation(nums1))


Solution()