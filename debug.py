class Solution:
    def maxArea(self, height) -> int:
        max = 0
        position_x = list(range(len(height)))
        for i in range(0, len(height) - 1):
            for j in range(i + 1, len(height)):
                height_min = min(height[i], height[j])
                distance_x = position_x[j] - position_x[i]
                #print(height_min* distance_x)
                if max < (height_min * distance_x):
                    max = (height_min * distance_x)
        return max
    def __init__(self):
        height=[1,8,6,2,5,4,8,3,7]
        result= self.maxArea(height)
        print(result)
Solution()
