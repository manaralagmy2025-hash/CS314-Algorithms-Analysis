# Insertion Sort Empirical Analysis

## 1. Overview
This project evaluates the performance of the **Insertion Sort** algorithm across three different input scenarios:
- **Best Case:** Already sorted array — running time is linear $\Omega(n)$ with minimal comparisons and zero shifts.
- **Worst Case:** Reverse-sorted array — running time is quadratic $O(n^2)$ with maximum comparisons and shifts.
- **Average Case:** Randomly ordered array — exhibits quadratic behavior $\Theta(n^2)$.

## 2. Experimental Setup
- Array sizes tested: $n \in [100, 500, 1000, 2000, 3000]$.
- Metrics tracked: Execution time (seconds), total comparisons, and element shifts.

## 3. Comparison with Merge Sort
While Insertion Sort is an in-place sorting algorithm that uses $O(1)$ auxiliary memory, its quadratic growth $O(n^2)$ makes it impractical for large datasets compared to Merge Sort's $O(n \log n)$ performance.
