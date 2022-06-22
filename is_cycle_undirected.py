def dfs(start,visited,parent,adj):
    visited[start]=True
    for neighbor in adj[start]:
        if visited[neighbor]==False:
            if dfs(neighbor,visited,start,adj):
                return True
        elif neighbor!=parent:
            return True
    return False
        


def is_cycle_undirected(v,adj):
    visited=[False for i in range(v)]
    for i in range(v):
        if visited[i]==False:
            if dfs(v,visited,-1,adj):
                return True
    return False
                
