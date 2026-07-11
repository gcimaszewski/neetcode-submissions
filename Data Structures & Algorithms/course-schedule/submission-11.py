class Solution:
    """
    Course Schedule

    You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

    The pair [0, 1], indicates that must take course 1 before taking course 0.

    There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

    Return true if it is possible to finish all courses, otherwise return false.
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # approach: do a DFS and detect a cycle
        # lightweight way to build the graph:
        # use an array of length numCourses, 
        # set g[i] = prequisite course for course i
        g_prereq = [[] for _ in range(numCourses)]
        for (crs, prq) in prerequisites:
            g_prereq[crs].append(prq)
        
        visited = set()
        path = set()
        def dfs_has_cycle(course):
            if course in path:
                return True
            if course in visited:
                return False
            path.add(course)
            for prereq in g_prereq[course]:
                if dfs_has_cycle(prereq):
                    return True
            path.remove(course)
            return False

        for course in range(numCourses):
            prqs = g_prereq[course]
            if dfs_has_cycle(course):
                return False
            # if prqs:
            #     has_cycle = dfs_has_cycle(course, set())
            #  #   print(f'course {course} has cycle: {has_cycle}')
            #     if has_cycle:
            #         return False

        return True