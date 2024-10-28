class DisjointSet:
    def __init__(self, vertices):
        # Initialize each vertex as a separate set
        self.parent = {v: v for v in vertices}
        # Initialize rank of each set to 0
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        # Find the root of the set (with path compression)
        if self.parent[item] != item:
            # Recursively find the root and update the parent
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        # Union by rank
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            # Attach smaller rank tree under root of higher rank tree
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            # Attach smaller rank tree under root of higher rank tree
            self.parent[yroot] = xroot
        else:
            # If ranks are same, make one as root and increment its rank
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

def kruskal_mst(graph):
    # Create a list of all edges in the graph
    edges = [(weight, u, v) for u in graph for v, weight in graph[u].items()]
    # Sort edges by weight in ascending order
    edges.sort()

    vertices = list(graph.keys())
    disjoint_set = DisjointSet(vertices)
    mst = []

    for weight, u, v in edges:
        # If including this edge doesn't create a cycle, add it to the MST
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append((u, v, weight))

        # Stop when we have V-1 edges in the MST (V is the number of vertices)
        if len(mst) == len(vertices) - 1:
            break

    return mst

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
        'E': {'C': 10, 'D': 2, 'F': 3},
        'F': {'D': 6, 'E': 3}
    }

    # Find the Minimum Spanning Tree
    mst = kruskal_mst(graph)

    # Print the edges in the Minimum Spanning Tree
    print("Edges in the Minimum Spanning Tree:")
    for edge in mst:
        print(f"{edge[0]} -- {edge[1]} : {edge[2]}")