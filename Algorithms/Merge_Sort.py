from random import randint

def merge_sort(arr):

	if len(arr) > 1:

		middle = len(arr) // 2

		L_arr = arr[:middle]
		R_arr = arr[middle:]

		merge_sort(L_arr)
		merge_sort(R_arr)

		i = j = k = 0

		while i < len(L_arr) and j < len(R_arr):

			if L_arr[i] < R_arr[j]:
				arr[k] = L_arr[i]
				i += 1
			else:
				arr[k] = R_arr[j]
				j += 1

			k += 1

		while i < len(L_arr):
			arr[k] = L_arr[i]
			i += 1
			k += 1

		while j < len(R_arr):
			arr[k] = R_arr[j]
			j += 1
			k += 1

	return arr


arr = [randint(0, 10) for x in range(10)]
print('Unsorted array:', arr)

sorted_arr = merge_sort(arr)
print('Sorted array:', sorted_arr)