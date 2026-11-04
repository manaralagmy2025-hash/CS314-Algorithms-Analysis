# Graph Traversal Algorithms: BFS, DFS, and Topological Sort

## 1. Overview
This laboratory implements and benchmarks fundamental graph traversal algorithms:
- **Breadth-First Search (BFS):** Layer-by-layer exploration computing unweighted shortest paths.
- **Depth-First Search (DFS):** Branch-by-branch exploration computing discovery ($d$) and finish ($f$) timestamps, alongside cycle detection.
- **Topological Sorting:** Linear ordering of vertices in a Directed Acyclic Graph (DAG) based on decreasing finish times.

## 2. Algorithm Comparison & Complexity
| Algorithm | Data Structure | Time Complexity (Adjacency List) | Space Complexity | Core Application |
| :--- | :---: | :---: | :---: | :--- |
| **BFS** | Queue (FIFO) | $\Theta(V + E)$ | $O(V)$ | Fewest-edges shortest path, layer traversal. |
| **DFS** | Stack / Recursion | $\Theta(V + E)$ | $O(V)$ | Cycle detection, topological sort, components. |
| **Topological Sort** | DFS + Ordered List | $\Theta(V + E)$ | $O(V)$ | Scheduling prerequisite tasks in DAGs. |

## 3. Representation Justification
The implementation utilizes an **Adjacency List** ($\Theta(V + E)$ space) instead of an **Adjacency Matrix** ($\Theta(V^2)$ space) because practical graphs are typically sparse ($|E| \ll |V|^2$), ensuring optimal linear time traversal.

## 4. Edge Classification & Cycle Detection
During DFS exploration of edge $(u, v)$:
- **White node:** Tree Edge (extends traversal).
- **Gray node:** Back Edge (indicates a **cycle**).
- **Black node:** Forward / Cross Edge.

## 5. Verification & Testing
The project includes automated tests for critical edge cases:
- Empty graphs and isolated vertices.
- Disconnected components.
- Cycle verification in directed graphs.
- Topological ordering validity check ensuring all directed edges satisfy $pos[u] < pos[v]$.
