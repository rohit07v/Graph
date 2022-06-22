
def helper(vertex,adj,visited,stack):
    visited[vertex]=True
    stack[vertex]=True
    for i in adj[vertex]:
        if visited[i]==True:
            if helper(i,adj,visited,stack):
                return True
        elif stack[i]:
            return True
    stack[vertex]=False
    return False
        




def is_cyclic_directed(v,adj):
    visited=[False for i in range(v+1)]
    stack = [False for i in range(v+1)]
    for i in range(v):
        if visited[i]==False:
            if helper(i,adj,visited,stack):
                return True
    return False
                
