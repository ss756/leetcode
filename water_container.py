class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     max = 0
    #     position_x = list( range(len(height)))
    #     for i in range(0,len(height)-1):
    #         for j in range( i+1, len(height)):
    #             height_min = min(height[i], height[j])
    #             distance_x = position_x[j] - position_x[i]
    #             if max< (height_min*distance_x):
    #                 max= (height_min*distance_x)
    #     return max
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            height_one = height[l]
            height_two = height[r]
            height_min = min(height_one, height_two)
            distance_x = r - l
            max_area = max(max_area, height_min * distance_x)
            if (height_one < height_two):
                l += 1
            else:
                r -= 1
        return max_area

    #     def maxArea(self, height: List[int]) -> int:
    #         l,r = 0, len(height)-1
    #         max_area = 0
    #         while(l<r):
    #             height_min= min(height[l],height[r] )
    #             max_area = max( max_area , height_min*(r-l))
    #             while(l<r and height_min == height[l]):
    #                 l+=1
    #             while(l<r and height_min == height[r]):
    #                 r-=1
    #         return max_area
    # def maxArea(self, height) -> int:
    #     l,r = 0, len(height)-1
    #     max_area=0
    #     while (l != r):
    #         if  (height[l] <=  height[r]):
    #             max_area = max(max_area, height[l]*(r-l))
    #             l+=1
    #         if (height[l] > height[r]):
    #             max_area = max(max_area, height[r]*(r-l))
    #             r-=1
    #     return max_area

    def __init__(self):
        height = [1,8,6,2,5,4,8,3,7]
        result= self.maxArea(height)
        print(result)
Solution()









