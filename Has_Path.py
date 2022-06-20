class Graph:

    def __init__(self,nvertices):
        self.nvertices = nvertices
        self.adjmatrix = [[0 for i in range(nvertices)]for j in range(nvertices)]


    def addEdge(self,v1,v2):
        self.adjmatrix[v1][v2]=1
        self.adjmatrix[v2][v1]=1

    def removeEdge(self,v1,v2):
        if not self.isEdge(v1,v2):
            return
        self.adjmatrix[v1][v2]=0
        self.adjmatrix[v2][v1]=0


    def isEdge(self,v1,v2):
        return True if self.adjmatrix[v1][v2]>0 else False


    def __hasPathhelper(self,v1,v2,visited):
        if self.adjmatrix[v1][v2]>0:
            return True
        visited[v1]=True
        flag = False
        for i in range(self.nvertices):
            if self.adjmatrix[v1][i]>0 and visited[i] is False:
                flag = self.__hasPathhelper(i,v2,visited)
                if flag is True:
                    return True
        return False

    
        
        




    def hasPath(self,v1,v2):
        if v1>= self.nvertices or v2>=self.nvertices:
            return False
        visited = [False for i in range(self.nvertices)]
        return self.__hasPathhelper(v1,v2,visited)

inp = [int(i) for i in input().strip().split(' ')]
# print(inp)
vertices = inp[0]
edges = inp[1]
g = Graph(vertices)
for i in range(edges):
    v = [int(i) for i in input().strip().split(' ')]
    g.addEdge(v[0],v[1])    

p = [int(i) for i in input().strip().split(' ')]
# print(p)
if g.hasPath(p[0],p[1]) is True:
    print('true')
else:
    print('false')
