# Divide and Conquer: Merge Sort vs Quicksort Analysis

## 1. Overview
This laboratory project implements and empirically analyzes two fundamental divide-and-conquer sorting algorithms: **Merge Sort** and **Quicksort** (using last-element pivot selection) as covered in Lecture 2.

## 2. Theoretical Complexity Summary
| Algorithm | Best Case | Average Case | Worst Case | Auxiliary Space | Stable? | In-Place? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Merge Sort** | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n)$ | Yes | No |
| **Quicksort** | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n^2)$ | $O(\log n)$ | No | Yes |

## 3. Implementation Details
- **Merge Sort:** Divides array at midpoint $q = \lfloor(p+r)/2\rfloor$ and combines sorted subarrays via `merge()` in $\Theta(n)$ time.
- **Quicksort:** Uses Lomuto partitioning (`PARTITION`) with $x = A[r]$ as pivot. No combine phase needed.
- **Test Coverage:** Validated across edge cases including empty lists, single items, duplicate values, sorted arrays, and reverse-sorted arrays.

## 4. Key Observations & Findings
1. **Stability & Space:** Merge Sort maintains the original relative order of duplicate keys (stable) but requires $\Theta(n)$ temporary memory. Quicksort sorts in place.
2. **Worst Case Breakdown:** Quicksort degenerates to $\Theta(n^2)$ on already sorted or reverse-sorted data when using the last element as pivot, whereas Merge Sort remains strictly $\Theta(n \log n)$ regardless of input ordering.
