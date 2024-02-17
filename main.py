import random
import timeit


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


# Перевірка реалізації
test_array_merge = [12, 11, 13, 5, 6, 7]
print("Merge sort test: ", merge_sort(test_array_merge))

test_array_insertion = [12, 11, 13, 5, 6, 7]
print("Insertion sort test: ", insertion_sort(test_array_insertion))


# Генерація тестових даних
small_random = [random.randint(0, 100) for _ in range(100)]
medium_random = [random.randint(0, 1000) for _ in range(1000)]
large_random = [random.randint(0, 10000) for _ in range(10000)]


# Вимірювання часу виконання для кожного алгоритму і розміру даних
def measure_time(arr, algorithm):
    arr_copy = arr.copy()
    if algorithm == "merge_sort":
        return timeit.timeit(lambda: merge_sort(arr_copy), number=1)
    elif algorithm == "insertion_sort":
        return timeit.timeit(lambda: insertion_sort(arr_copy), number=1)
    elif algorithm == "timsort":
        return timeit.timeit(lambda: sorted(arr_copy), number=1)


# Вимірювання часу для різних алгоритмів і розмірів даних
results = {}
for size, arr in [
    ("small", small_random),
    ("medium", medium_random),
    ("large", large_random),
]:
    for alg in ["merge_sort", "insertion_sort", "timsort"]:
        key = f"{alg}_{size}"
        results[key] = measure_time(arr, alg)

print(results)
