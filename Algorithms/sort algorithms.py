def insertion_sort(array):

	for i in range(len(array)):
		key = array[i]
		j = i - 1

		while j >= 0 and key < array[j]:
			array[j + 1] = array[j]
			j -= 1

		array[j + 1] = key

	return array


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


if __name__ == '__main__':

	# Insertion Sort
	array = [5, 2, 4, 6, 1, 3]
	print(f'Insertion Sort {array}: {insertion_sort(array)}')

	# Merge Sort
	array = [5, 2, 4, 7, 1, 3, 2, 6]
	print(f'Merge Sort {array}: {merge_sort(array)}')