class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        '''
        Here we have to see that there are four cases possible
        kill 3 biggest elements
        kill 3 biggest elements
        kill 2 biggest elements + 1 smallest elements
        kill 1 biggest elements + 2 smallest elements
        kill 3 smallest elements
        '''
        return min([b-a for a, b in zip(nums[:4], nums[-4:])])