import random
import math


def left(i):
	return i * 2


def right(i):
	return (i * 2) + 1


def parent(i):
	return math.floor(i)


def max_heapify(arr, i, n):

	l = left(i)
	r = right(i)
	largest = i

	if (l < n) and arr[l] >= arr[largest]:
		largest = l
	if (r < n) and arr[r] >= arr[largest]:
		largest = r

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		max_heapify(arr, largest, n)


def min_heapify(arr, i, n):

	l = left(i)
	r = right(i)
	smallest = i

	if (l < n) and arr[l] <= arr[smallest]:
		smallest = l
	if (r < n) and arr[r] <= arr[smallest]:
		smallest = r

	if smallest != i:
		arr[i], arr[smallest] = arr[smallest], arr[i]
		min_heapify(arr, smallest, n)


def build_max_haep(arr, n):

	for i in range(n // 2 - 1, -1, -1):
		max_heapify(arr, i, n)

	for i in range(n - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		max_heapify(arr, 0, i)


def build_min_haep(arr, n):
	
	for i in range(math.floor(n // 2), 0, -1):
		min_heapify(arr, i, n)

	for i in range(n - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		min_heapify(arr, 0, i)


def extract_max_from_max_heap(arr, n):

	if n == 0:
		raise Exception('Empty Array')

	max = arr[0]
	arr[0] = arr[n - 1]
	max_heapify(arr, 0, n - 1)
	return max


def extract_min_from_max_heap(arr, n):

	if n == 0:
		raise Exception('Empty Array')

	min = arr[0]
	arr[0] = arr[n - 1]
	min_heapify(arr, 0, n - 1)
	return min


def heap_increase_key(arr, i, key):

	if key < arr[i]:
		print('Key is smaller than old key!')
		return

	arr[i] = key
	while i > 0 and arr[parent(i)] < arr[i]:
		arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
		i = parent(i)


def insert_into_max_heap(arr, key, n):

	arr = arr + [0]
	heap_increase_key(arr, n, key)
	return arr




if __name__ == '__main__':

	arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

	# Build Key
	build_max_haep(arr, len(arr))
	print('Max Heap:', arr[::-1])

	# Get Max key
	print('Max:', extract_max_from_max_heap(arr[::-1], len(arr)))

	# Replace key
	i, key = 4, random.randint(0, len(arr))
	old_val = arr[i]	
	heap_increase_key(arr, i, key)
	print('Changed value {0} with {1}: {2}'.format(old_val, key, arr[::-1]))

	# Insert
	val = 3
	arr = insert_into_max_heap(arr, val, len(arr))
	print('Inserted {0} into Heap: {1}'.format(val, arr[::-1]))