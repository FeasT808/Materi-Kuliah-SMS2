import time
import random


size = 10000
data = sorted(random.sample(range(size * 10), size))

# Algoritma Linear Search
def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

# Algoritma Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons

# Skenario Uji
targets = {
    "Worst-case": data[-1],  # Target di posisi terakhir
    "Best-case": data[0],  # Target di posisi pertama
    "Average-case": random.choice(data)  # Target acak di tengah
}

scenarios = list(targets.keys())
linear_times, binary_times = [], []
linear_comparisons, binary_comparisons = [], []

print(f"=== Uji Search - Data Size: {size} ===")

for case, target in targets.items():
    print(f"\n[{case}] Target: {target}")

    start = time.time()
    _, linear_cmp = linear_search(data, target)
    linear_time = time.time() - start

    start = time.time()
    _, binary_cmp = binary_search(data, target)
    binary_time = time.time() - start

    print(f"Linear Search > Time: {linear_time:.6f}s | Comparisons: {linear_cmp}")
    print(f"Binary Search > Time: {binary_time:.6f}s | Comparisons: {binary_cmp}")
