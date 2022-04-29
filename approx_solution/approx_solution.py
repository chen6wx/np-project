'''
    name: Alex Guilliams
    Approximation code for Vertex Cover.
    Used code/information from:
    https://www.geeksforgeeks.org/vertex-cover-problem-set-1-introduction-approximate-algorithm-2/
    http://tandy.cs.illinois.edu/dartmouth-cs-approx.pdf

'''

from collections import defaultdict
g = {}

def addEdges(u, vertices):
    if u not in g:
        g[u] = []
    for v in vertices:
        g[u].append(v)

def approxVertexCover(g):
        
    amount = len(g)
    # Initialize all vertices as not visited.
    visited = [False] * (amount)
        
    # Consider all edges one by one
    for u in range(amount):
            
        # An edge is only picked when
        # both visited[u] and visited[v]
        # are false
        if not visited[u]:
                
            # Go through all adjacents of u and
            # pick the first not yet visited
            # vertex (We are basically picking
            # an edge (u, v) from remaining edges.
            for v in g[u]:
                if not visited[v]:
                        
                    # Add the vertices (u, v) to the
                    # result set. We make the vertex
                    # u and v visited so that all
                    # edges from/to them would
                    # be ignored
                    visited[v] = True
                    visited[u] = True
                    break

    # Print the vertex cover
    for j in range(amount):
        if visited[j]:
            print(j, end = ' ')
                 
    print()

def main():

    n = int(input())
    lines = [[int(x) for x in input().split()] for _ in range(n)]
    for line in lines:
        addEdges(line[0], line[1:])
    approxVertexCover(g)

if __name__ == "__main__":
    main()
