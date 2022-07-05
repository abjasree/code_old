import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = - sqrt(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        return [[x,y] for (dist, x, y) in heap]
    
    def brute_force_kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_list = []
        for ele in points:
            distance = sqrt(ele[0]**2 + ele[1]**2)
            distance_list.append(round(distance, 3))
        arg_list =[idx for idx,ele in sorted(enumerate(distance_list), key = lambda idx: idx[1])]
        
        result = []
        for i in range(k):
            result.append(points[arg_list[i]])
        return result
        
            
        
            
            
        