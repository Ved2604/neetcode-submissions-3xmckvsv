from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = deque()
        for i in range(len(nums)):
            if queue and queue[0] <= i - k:   ## should this if statment not be a loop ? that like removes all the leftmost elements out of window 
            # also that means the queue has intermediate elements that are outside the window not queue[0] or queue[-1] 
                
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result





        
                

        