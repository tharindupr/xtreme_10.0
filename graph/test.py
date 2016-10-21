"""q=input()
for i in range(q):
    nm=raw_input().strip().split(" ")
    v=int(nm[0])
    e=int(nm[1])
    for j in range(e):"""


graph = {'A': set(['B', 'C']),
                 'B': set(['A', 'D', 'E']),
                 'C': set(['A', 'F']),
                 'D': set(['B']),
                 'E': set(['B', 'F']),
                 'F': set(['C', 'E'])}

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

bfs(graph, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}