import time
import random
import math

# متغير عام لحساب عدد المقارنات أثناء عمليات الـ Heap
comparisons_count = 0

def heapify(arr, n, i):
    """
    إصلاح خاصية الـ Max-Heap لعنصر عند الفهرس i داخل مصفوفة حجم الهيب فيها n
    """
    global comparisons_count
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # التحقق من الابن الأيسر
    if left < n:
        comparisons_count += 1
        if arr[left] > arr[largest]:
            largest = left

    # التحقق من الابن الأيمن
    if right < n:
        comparisons_count += 1
        if arr[right] > arr[largest]:
            largest = right

    # التبديل والاستمرار إذا لم يكن الجذر هو الأكبر
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_max_heap(arr):
    """
    بناء Max-Heap بالبدء من آخر أب وصولاً للجذر بتعقيد O(n)
    """
    n = len(arr)
    # البدء من آخر عقدة غير ورقية (n // 2 - 1)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    """
    ترتيب المصفوفة تصاعدياً في المكان (In-place) بتعقيد O(n log n)
    """
    global comparisons_count
    a = arr.copy()
    n = len(a)

    # 1. بناء الهيب الأقصى
    build_max_heap(a)

    # 2. استخراج العنصر الأقصى وتبديله مع النهاية ثم إصلاح الهيب
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        heapify(a, end, 0)

    return a

# ==================== اختبار صحة الكود ====================
def run_unit_tests():
    test_cases = {
        "Empty array": [],
        "Single element": [9],
        "Duplicates": [5, 2, 8, 5, 2, 9, 8],
        "Already sorted": [1, 2, 3, 4, 5, 6, 7],
        "Reverse sorted": [9, 8, 7, 6, 5, 4, 3]
    }
    print("=== Running Unit Tests ===")
    for name, test in test_cases.items():
        sorted_result = heap_sort(test)
        assert sorted_result == sorted(test), f"Test failed for {name}"
        print(f"PASS: {name}")
    print("All unit tests passed successfully!\n")

# ==================== قياس الأداء ====================
def run_benchmark():
    global comparisons_count
    sizes = [1000, 5000, 10000, 25000, 50000]

    print(f"{'Size (n)':<10} | {'Time (sec)':<12} | {'Comparisons':<14} | {'Theoretical (n log2 n)':<22}")
    print("-" * 65)

    for n in sizes:
        data = [random.randint(1, 1000000) for _ in range(n)]
        comparisons_count = 0

        start_time = time.perf_counter()
        heap_sort(data)
        elapsed_time = time.perf_counter() - start_time

        theoretical_nlogn = int(n * math.log2(n))
        print(f"{n:<10} | {elapsed_time:<12.5f} | {comparisons_count:<14} | {theoretical_nlogn:<22}")

if __name__ == "__main__":
    run_unit_tests()
    run_benchmark()
