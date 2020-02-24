# https://leetcode.com/problems/critical-connections-in-a-network/description/

from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        graph = defaultdict(list)

        # create adjacency list T O(n)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        # earliestVertexReachable for each vertex; 0 for all unvisited node
        low = [0] * n

        def dfs(rank, current, parent):
            low[current] = rank
            ans = []

            for child in graph[current]:

                if child == parent:
                    continue

                # unvisited node
                elif low[child] == 0:
                    ans += dfs(rank + 1, child, current)

                low[current] = min(low[current], low[child])

                # if true then current parent to child is the only connection to the child, hence a bridge
                if low[child] > rank:
                    ans.append([child, current])

            # return bridge indices up to the dfs invoking call
            return ans

        return dfs(1, 0, -1)

    # T O(V+E) = n+n^2 = O(n^2) S O(n^2)

#  DFS time complexity is O(|E| + |V|), attempting to visit each edge at most twice. (the second attempt will immediately return.)
# As the graph is always a connected graph, |E| >= |V|.

# So, time complexity = O(|E|). O(n^2)

# Space complexity = O(graph) + O(low)  = O(V+E) + O(V) = O(n^2)


