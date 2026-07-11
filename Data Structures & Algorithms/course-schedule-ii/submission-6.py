class Solution:
    """
    Course Schedule II
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # approach: use DFS to perform a topological sort of the courses
        # if we detect a cycle, return []

        # create adjacency list
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visited = set()
        path = set()
        # node_to_finished_time = {}
        ordering = []
        def dfs_topo_sort(node):
            if node in path: # cycle!
                return True
            if node in visited:
                # we already did the prerequisite course; exit
                return False
            
            path.add(node)
            for prereq in adj[node]:
                if dfs_topo_sort(prereq):
                    return True
            path.remove(node)
            visited.add(node)
            ordering.append(node)
            return False

        for course_idx, prereqs in enumerate(adj):
            if dfs_topo_sort(course_idx):
                return []
        return ordering

