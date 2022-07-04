class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        result = []
        for ele in intervals:
            if result == [] or result[-1][1] < ele[0]:
                result.append(ele)
            else:
                result[-1][1] = max(result[-1][1], ele[1])
                
        return result
            
        