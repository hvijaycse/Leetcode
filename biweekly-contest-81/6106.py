from typing import List, Optional, Any, Dict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        adjencyList = {
            i: [] for i in range(n)
        }
        visited = {
            i: False for i in range(n)
        }

        for n1, n2 in edges:
            adjencyList[n1].append(n2)
            adjencyList[n2].append(n1)
            

        graphs = []

        for node in adjencyList.keys():
            if not visited[node]:
                count = self.bfs( node, adjencyList, visited)
                graphs.append(count)
        graphs.append(0)
        reverseSum = list(graphs)

        for i in range(len(graphs)-2, -1, -1):
            reverseSum[i] += reverseSum[i+1]
        
        totalpairs = 0
        for i in range(len(graphs) -1):
            totalpairs += graphs[i] * reverseSum[i+1]
        
        return totalpairs

    
    def bfs(self, node, adjencyList, visited):

        edgeCount = 0 

        queue = [node]

        while queue:
            currentNode = queue.pop(0)
            if  visited[currentNode]:
                continue

            edgeCount += 1
            visited[currentNode] = True
            for neighbour in adjencyList[currentNode]:
                queue.append(neighbour)
        
        return edgeCount