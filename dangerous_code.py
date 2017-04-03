# adding more dangerous code
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),}
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        # if vertex not in visited:
        visited.add(vertex)
        stack.extend(graph[vertex] - visited)
        print(vertex,stack)
    return visited

dfs(graph, 'A') 
# more changes...
