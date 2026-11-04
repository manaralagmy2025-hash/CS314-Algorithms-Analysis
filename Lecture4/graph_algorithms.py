from collections import deque
import time
import random

class Graph:
    def __init__(self, directed=False):
        self.adj = {}
        self.directed = directed

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def add_vertex(self, u):
        if u not in self.adj:
            self.adj[u] = []

    # ==================== 1. Breadth-First Search ====================
    def bfs(self, s):
        if s not in self.adj:
            return {}, {}
        
        dist = {u: float('inf') for u in self.adj}
        parent = {u: None for u in self.adj}
        dist[s] = 0
        
        q = deque([s])
        while q:
            u = q.popleft()
            for v in self.adj[u]:
                if dist[v] == float('inf'):
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
        return dist, parent

    # ==================== 2. Depth-First Search ====================
    def dfs(self):
        # 0: WHITE, 1: GRAY, 2: BLACK
        color = {u: 0 for u in self.adj}
        d = {}
        f = {}
        parent = {u: None for u in self.adj}
        has_cycle = [False]
        t = [0]

        def dfs_visit(u):
            t[0] += 1
            d[u] = t[0]
            color[u] = 1  # GRAY

            for v in self.adj[u]:
                if color[v] == 1:
                    has_cycle[0] = True  # Back edge detected
                elif color[v] == 0:
                    parent[v] = u
                    dfs_visit(v)

            color[u] = 2  # BLACK
            t[0] += 1
            f[u] = t[0]

        for u in self.adj:
            if color[u] == 0:
                dfs_visit(u)

        return d, f, parent, has_cycle[0]

    # ==================== 3. Topological Sort ====================
    def topological_sort(self):
        if not self.directed:
            raise ValueError("Topological sort applies only to DAGs (Directed Graphs).")
        
        d, f, _, has_cycle = self.dfs()
        if has_cycle:
            return None  # Cycle detected, impossible to order
        
        # Order vertices by decreasing finish time
        return sorted(f.keys(), key=lambda node: f[node], reverse=True)


# ==================== Unit Testing ====================
def run_unit_tests():
    print("=== Running Unit Tests ===")
    
    # 1. Empty Graph
    g_empty = Graph()
    assert g_empty.bfs("A") == ({}, {})
    print("PASS: Empty Graph")

    # 2. Single Vertex
    g_single = Graph()
    g_single.add_vertex("A")
    dist, _ = g_single.bfs("A")
    assert dist["A"] == 0
    print("PASS: Single Vertex Graph")

    # 3. Disconnected Graph
    g_disc = Graph(directed=False)
    g_disc.add_edge("A", "B")
    g_disc.add_edge("C", "D")
    dist, _ = g_disc.bfs("A")
    assert dist["B"] == 1 and dist["C"] == float('inf')
    print("PASS: Disconnected Graph")

    # 4. Cycle Detection
    g_cycle = Graph(directed=True)
    g_cycle.add_edge("A", "B")
    g_cycle.add_edge("B", "C")
    g_cycle.add_edge("C", "A")
    _, _, _, has_cycle = g_cycle.dfs()
    assert has_cycle == True
    assert g_cycle.topological_sort() is None
    print("PASS: Cycle Detection in Directed Graph")

    # 5. DAG and Topological Sort (Slide 58 example)
    g_dag = Graph(directed=True)
    edges = [("A", "B"), ("B", "D"), ("D", "F"), ("A", "C"), ("C", "E"), ("E", "F"), ("C", "D")]
    for u, v in edges:
        g_dag.add_edge(u, v)
    topo_order = g_dag.topological_sort()
    assert topo_order is not None
    # Verify every edge goes forward
    pos = {node: i for i, node in enumerate(topo_order)}
    for u, v in edges:
        assert pos[u] < pos[v]
    print(f"PASS: Topological Sort -> {topo_order}")
    print("All unit tests passed successfully!\n")


# ==================== Empirical Benchmarking ====================
def run_benchmark():
    print(f"{'Vertices (V)':<14} | {'Edges (E)':<12} | {'V + E':<12} | {'BFS Time (s)':<14} | {'DFS Time (s)':<14}")
    print("-" * 72)

    sizes = [(1000, 3000), (5000, 15000), (10000, 30000), (20000, 60000)]
    for v_count, e_count in sizes:
        g = Graph(directed=False)
        for i in range(v_count):
            g.add_vertex(i)
        
        # Add random edges
        for _ in range(e_count):
            u = random.randint(0, v_count - 1)
            v = random.randint(0, v_count - 1)
            g.add_edge(u, v)

        # Time BFS
        start = time.perf_counter()
        g.bfs(0)
        t_bfs = time.perf_counter() - start

        # Time DFS
        start = time.perf_counter()
        g.dfs()
        t_dfs = time.perf_counter() - start

        print(f"{v_count:<14} | {e_count:<12} | {v_count + e_count:<12} | {t_bfs:<14.5f} | {t_dfs:<14.5f}")

if __name__ == "__main__":
    run_unit_tests()
    run_benchmark()
