from typing import List, Optional, Any, Dict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        '''
        Tarjan's Algorithm
        '''


        grid = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        lowest = [ _ for _ in range(n)]

        for connection in connections:
            grid[connection[0]].append(connection[1])
            grid[connection[1]].append(connection[0])
        
        # for row in grid:
        #     print(row)
        
        def dfs(res, currentVertex, previous, level):

            lowest[currentVertex] = level
            visited[currentVertex] = True
            # print(f"Node: {currentVertex}, level:{lowest[currentVertex]}")

            for nextVertex in grid[currentVertex]:
                if nextVertex==previous:
                    continue
                if not visited[nextVertex]:
                    dfs(res, nextVertex, currentVertex, level+1)

                lowest[currentVertex] = min(lowest[currentVertex], lowest[nextVertex])

                if lowest[nextVertex] >= level + 1:
                    res.append([currentVertex, nextVertex])            
            # print(f"Node: {currentVertex}, level:{lowest[currentVertex]}")
        
        res = []
        dfs(res, 0,-1, 0)

        return res
            
