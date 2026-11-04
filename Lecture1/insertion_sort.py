import time
import random

def insertion_sort(arr):
    comparisons = 0
    shifts = 0
    a = arr.copy()
    
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key
        
    return a, comparisons, shifts

def run_experiment():
    sizes = [100, 500, 1000, 2000, 3000]
    print(f"{'Size (n)':<10} | {'Type':<12} | {'Time (sec)':<12} | {'Comparisons':<12} | {'Shifts':<12}")
    print("-" * 65)

    for n in sizes:
        sorted_arr = list(range(n))
        reverse_arr = list(range(n, 0, -1))
        random_arr = [random.randint(1, 10000) for _ in range(n)]

        for arr_type, data in [("Sorted", sorted_arr), ("Reverse", reverse_arr), ("Random", random_arr)]:
            start_time = time.perf_counter()
            _, comps, shifts = insertion_sort(data)
            elapsed = time.perf_counter() - start_time
            print(f"{n:<10} | {arr_type:<12} | {elapsed:<12.5f} | {comps:<12} | {shifts:<12}")

if __name__ == "__main__":
    run_experiment()
