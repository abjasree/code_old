class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        visited = [0 for i in range(numCourses)]
        for prereq in prerequisites:
            c1, c2 = prereq
            graph[c1].append(c2)
            
        for i in range(numCourses):
            if not self.helper(visited, graph, i):
                return False
        return True
        
        
    def helper(self, visited, graph, i):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for j in graph[i]:
            if not self.helper(visited, graph, j):
                return False
        visited[i] = 1
        return True
        