class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nge = {}   # next greater element map
        
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                nge[prev] = num
            stack.append(num)
        
        while stack:
            nge[stack.pop()] = -1

        result = []
        for num in nums1:
            result.append(nge[num])
            
        return result