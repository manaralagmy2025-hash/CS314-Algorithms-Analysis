import time
import random
import sys

# زيادة حد التكرار لتفادي RecursionError مع Quicksort في الحالة العكسية
sys.setrecursionlimit(20000)

# ==================== 1. Merge Sort ====================
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(L, R):
    out = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            out.append(L[i])
            i += 1
        else:
            out.append(R[j])
            j += 1
    return out + L[i:] + R[j:]

# ==================== 2. Quicksort ====================
def quicksort(arr):
    a = arr.copy()
    _quicksort_helper(a, 0, len(a) - 1)
    return a

def _quicksort_helper(a, p, r):
    if p < r:
        q = partition(a, p, r)
        _quicksort_helper(a, p, q - 1)
        _quicksort_helper(a, q + 1, r)

def partition(a, p, r):
    x = a[r]  # Last-element pivot as instructed in lecture
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1

# ==================== 3. Testing Cases ====================
def run_tests():
    test_cases = {
        "Empty": [],
        "Single": [42],
        "Duplicates": [4, 2, 4, 3, 2, 4, 1],
        "Already Sorted": [1, 2, 3, 4, 5, 6],
        "Reverse Sorted": [6, 5, 4, 3, 2, 1]
    }
    print("=== Testing Correctness ===")
    for name, case in test_cases.items():
        assert merge_sort(case) == sorted(case), f"MergeSort failed on {name}"
        assert quicksort(case) == sorted(case), f"QuickSort failed on {name}"
        print(f"PASS: {name} array")
    print("All tests passed successfully!\n")

# ==================== 4. Benchmarking ====================
def benchmark():
    sizes = [1000, 2000, 5000]
    print(f"{'Size (n)':<10} | {'Input Type':<12} | {'Merge Sort (s)':<16} | {'Quicksort (s)':<16}")
    print("-" * 62)

    for n in sizes:
        inputs = {
            "Random": [random.randint(1, 100000) for _ in range(n)],
            "Sorted": list(range(n)),
            "Reverse": list(range(n, 0, -1))
        }

        for input_type, data in inputs.items():
            # قياس زمن Merge Sort
            start = time.perf_counter()
            merge_sort(data)
            t_merge = time.perf_counter() - start

            # قياس زمن Quicksort
            # ملاحظة: تم استبعاد الأحجام الكبيرة جداً للحالة العكسية تجنباً للبطء التربيعي O(n^2)
            if input_type in ["Sorted", "Reverse"] and n > 2000:
                t_quick_str = "O(n^2) skipped"
            else:
                start = time.perf_counter()
                quicksort(data)
                t_quick = time.perf_counter() - start
                t_quick_str = f"{t_quick:.5f}"

            print(f"{n:<10} | {input_type:<12} | {t_merge:<16.5f} | {t_quick_str:<16}")

if __name__ == "__main__":
    run_tests()
    benchmark()
