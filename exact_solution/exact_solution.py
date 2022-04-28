'''
    name: Andrew Toske
    Exact code for Vertex Cover.
    Used code/information from:
    https://www.delftstack.com/howto/python/powerset-python/
'''
graph = {}
edges = []

#Add edge to graph
def addEdges(u, vertices):
    if u not in graph:
        graph[u] = []
    for v in vertices:
        graph[u].append(v)
        edge = sorted([u, v])
        if edge not in edges:
            edges.append(edge)

#Find all subsets for given vertices - O(2^V)
def subs(vertices):
    if vertices == []:
        return [[]]
    x = subs(vertices[1:])
    return x + [[vertices[0]] + y for y in x]

#Check if given vertices cover every edge
def covers(graph, vertices):
    visited_edges = []
    for u in vertices:
        for v in graph[u]:
            edge = sorted([u, v])
            if edge not in visited_edges:
                visited_edges.append(edge)
    if len(visited_edges) != len(edges): 
        return False
    return True

# Driver Code
def main():
    # addEdges(0, [1, 2])
    # addEdges(1, [0, 3])
    # addEdges(2, [0])
    # addEdges(3, [1, 4])
    # addEdges(4, [3, 5])
    # addEdges(5, [4, 6])
    # addEdges(6, [5])

    # addEdges(0, [2])
    # addEdges(1, [4])
    # addEdges(2, [0, 4])
    # addEdges(3, [4])
    # addEdges(4, [1, 2, 3])

    addEdges(0, [1])
    addEdges(1, [11, 8])
    addEdges(2, [11, 14])
    addEdges(3, [12, 4])
    addEdges(4, [3, 5])
    addEdges(5, [9, 4])
    addEdges(6, [10])
    addEdges(7, [10])
    addEdges(8, [1, 10])
    addEdges(9, [13, 5])
    addEdges(10, [8, 7, 6])
    addEdges(11, [1, 2, 13])
    addEdges(12, [3, 13])
    addEdges(13, [14, 11, 12, 9, 10])
    addEdges(14, [2, 13])

    min = float('inf')
    min_vertices = []
    subsets = subs([*graph])
    for subset in subsets:
        if covers(graph, subset):
            n = len(subset)
            if n < min:
                min = n
                min_vertices = subset
    print(min)
    print(min_vertices)



 
if __name__ == "__main__":
    main()