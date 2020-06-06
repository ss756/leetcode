class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
            ans=[]
            def perm(nums,start):
                if start==len(nums)-1:
                    ans.append(nums)
                    return
                for j in range(start,len(nums)):
                    nums[j],nums[start]=nums[start],nums[j] #swapping the elements
                    perm(nums[:],start+1)  # nums[:] = nums.copy() i.e, just makes the duplicate of the current array
            perm(nums,0)
            return ans