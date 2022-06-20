from sys import stdin
import queue
class Graph:

    def __init__(self,nvertices):
        self.nvertices=nvertices
        self.adjmatrix = [[False for i in range(nvertices)]for j in range(nvertices)]

    def addedge(self,v1,v2):
        self.adjmatrix[v1][v2]=1
        self.adjmatrix[v2][v1]=1


    def removeedge(self,v1,v2):
        if not self.isedge(v1,v2):
            return
        self.adjmatrix[v1][v2]=0
        self.adjmatrix[v2][v1]=0

    def isedge(self,v1,v2):
        return True if adjmatrix[v1][v2]>0 else False


    def __bfshelper(self,vertex,visited):
        q=queue.Queue()
        q.put(vertex)
        visited[vertex]=True
        while not q.empty():
            v = q.get()
            print(v,end=" ")
            for i in range(self.nvertices):
                if self.adjmatrix[v][i] and not visited[i]:
                    q.put(i)
                    visited[i]=True
                    

            
    

    def bfs_path(self):
        visited = [False for i in range(self.nvertices)]
        for i in range(self.nvertices):
            if not visited[i]:
                self.__bfshelper(i,visited)

                
li = stdin.readline().strip().split()

V = int(li[0])

E = int(li[1])

g = Graph(V)

for i in range(E) :

    arr = stdin.readline().strip().split()

    fv = int(arr[0])

    sv = int(arr[1])

    g.addedge(fv, sv)

g.bfs_path()



def bfs(v,adj):
    ans = []
    visited=[False for i in range(v)]
    q=queue.Queue()
    q.put(0)
    visited[0]=True
    while not q.empty():
        x = q.get()
        ans.append(x)
        for i in adj[v]:
            if visited[i]==False:
                visited[i]=True
                q.put(i)
    return ans


