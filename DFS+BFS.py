from collections import deque

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(visited, graph, neighbour)

def bfs(visited, graph, start):
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for i in range(1, n+1):
        edges = int(input(f"Enter number of edges for node {i}: "))
        graph[i] = []
        for j in range(edges):
            dest = int(input(f"Enter edge {j+1} for node {i}: "))
            graph[i].append(dest)
            if dest not in graph:
                graph[dest] = []

    print("The following is DFS:")
    dfs(set(), graph, 1)

    print("\nThe following is BFS:")
    bfs(set(), graph, 1)

if __name__ == '__main__':
    main()
