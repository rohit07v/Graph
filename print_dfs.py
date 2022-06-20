class Graph:
    def __init__(self,nvertices):
        self.nvertices = nvertices
        self.adjmatrix = [[False for i in range(nvertices)] for j in range(nvertices)]


    def addedge(self,v1,v2):
        self.adjmatrix[v1][v2] = 1
        self.adjmatrix[v2][v1] = 1

    def removeedge(self,v1,v2):
        if not self.isEdge(v1,v2):
            return
        self.adjmatrix[v1][v2] = 0
        self.adjmatrix[v2][v1] = 0

    def isEdge(self,v1,v2):
        return True if self.adjmatrix[v1][v2]>0 else False

    def __str__(self):
        return str(self.adjmatrix)
    
    def __printdfs(self,v1,v2,visited):
        visited[v1]=True
        if v1==v2:
            return [v1]
        for i in range(self.nvertices):
            if self.isEdge(v1,i) and not visited[i]:
                visited[i]=True
                ans = self.__printdfs(i,v2,visited)
                if ans:
                    ans.append(v1)
                    return ans
        return []


    
    def print_dfs(self,v1,v2):
        visited = [False for i in range(self.nvertices)]
        return self.__printdfs(v1,v2,visited)


    

num_of_vertices,num_of_edges = [int(i) for i in input().strip().split()]
g = Graph(num_of_vertices)
for i in range(num_of_edges):
    v1,v2 = [int(i) for i in input().strip().split()]
    g.addedge(v1,v2)
    
v1,v2 = [int(i) for i in input().strip().split()]
ans = g.print_dfs(v1,v2)
if ans:
    for i in ans:
        print(i,end=' ')
















def printdfs(self,v,adjmatrix):
    def helper(v):
        visited[v]=True
        ans.append(v)
        for i in range(adj[v]):
            if visited[i]==False:
                helper(i)
    ans = []
    visited = [False for i in range(V)]
    helper(0)
    return ans
    
        
