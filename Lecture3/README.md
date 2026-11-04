# Heap Sort Analysis & Priority Queue Foundations

## 1. Overview
This project presents an empirical and theoretical analysis of **Heap Sort** using a binary **Max-Heap**, covering the core operations: `heapify`, `build_max_heap`, and `heap_sort` as detailed in Lecture 3.

## 2. Algorithm Characteristics & Complexity
| Phase / Property | Complexity | Description |
| :--- | :---: | :--- |
| **BUILD-MAX-HEAP** | $\Theta(n)$ | Linear time construction by bottom-up heapification from $\lfloor n/2 \rfloor$ down to root. |
| **MAX-HEAPIFY** | $O(\log n)$ | Sinks an invalid root down the tree along a single path of height $h \le \lfloor \log_2 n \rfloor$. |
| **HEAPSORT** | $\Theta(n \log n)$ | Guaranteed $O(n \log n)$ time in best, average, and worst cases. |
| **Auxiliary Memory** | $O(1)$ | Strictly in-place algorithm requiring no secondary dynamic buffers. |
| **Stability** | No | Unstable due to long-distance swaps across array levels. |

## 3. Comparison with Other Sorts
- **Versus Merge Sort:** Merge sort guarantees $O(n \log n)$ and is stable, but requires $\Theta(n)$ auxiliary space. Heap sort matches the time guarantee while remaining strictly $O(1)$ in-place.
- **Versus Quicksort:** While Quicksort can degrade to $O(n^2)$ on worst-case inputs, Heap sort maintains a rigid $O(n \log n)$ bound. However, Quicksort typically runs faster in practice due to contiguous memory access and CPU cache friendliness.

## 4. Verification & Testing
The code contains unit tests verifying edge cases:
- Empty lists and single elements.
- Datasets with heavy duplicates.
- Already sorted and reverse-ordered collections.
- Comparison metrics verifying empirical comparison counts scale proportionally with $n \log_2 n$.
