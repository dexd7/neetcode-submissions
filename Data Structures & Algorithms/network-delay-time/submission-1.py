class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append([v,t])
        total_times = [float('inf')] * (n+1)
        total_times[0] = 0
        def dfs(node,  time):
            if time>=total_times[node]:
                return
            total_times[node] = time
            for nei, weight in adj[node]:
                dfs(nei, time+weight)


        
        dfs(k, 0)
        res = max(total_times)
        return res if res != float('inf') else -1
