from collections import deque
def add_vertex(v):
    global graph
    graph[v]=[]
def add_edge(v1,v2):
    global graph
    graph[v1].append(v2)
def bfs(node):
    global graph
    global visited
    global q
    visited.append(node)
    q.append(node)
    while q:
        s=q.popleft()
        print(s,end=" ")
        for adj_vertices in graph[s]:
            if adj_vertices not in visited:
                visited.append(adj_vertices)
                q.append(adj_vertices)
    
    

graph={}
visited=deque()

q=deque()
add_vertex(0)
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)
add_vertex(5)
add_vertex(6)
add_vertex(7)
add_vertex(8)

add_edge(0,1)
add_edge(0,3)
add_edge(0,4)
add_edge(1,2)
add_edge(1,4)
add_edge(2,5)
add_edge(3,4)
add_edge(3,6)
add_edge(4,5)
add_edge(4,7)
add_edge(6,4)
add_edge(6,7)
add_edge(7,5)
add_edge(7,8)

print(graph)
bfs(1)
