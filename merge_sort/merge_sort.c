#include <stdio.h>
#include <stdlib.h>


void printArray(int array[], int size) {
	for ( int i = 0; i < size; i++) {
		printf("%d, ", array[i]);
	};
	printf("\n");
}


int mergeLists(int list_to_sort[], int start_a, int start_b, int end_b) {
	int len_a = start_b - start_a;
	int len_b = end_b - start_b + 1;
	int a[len_a], b[len_b];
	int i = 0; int j = 0;
	for (i; i < len_a; i++) {
		a[i] = list_to_sort[start_a + i];
	}
	for (j; j < len_b; j++) {
		b[j] = list_to_sort[start_b + j];
	}
	i = 0; j = 0; int target_ix = start_a;
	while ( (i < len_a) && (j < len_b) ) {
		// replace places in the list to sort according to order
		if (a[i] < b[j]) {
			list_to_sort[target_ix] = a[i];
			i++;
		} else {
			list_to_sort[target_ix] = b[j];
			j++;
		}
		target_ix++;
	}

	if (i < len_a) {
		for (i; i < len_a; i++) {
			list_to_sort[target_ix] = a[i];
			target_ix++;
		}
	} else if (j < len_b) {
		for (j; j < len_b; j++) {
			list_to_sort[target_ix] = b[j];
			target_ix++;
		}
	}
}


void mergeSort(int list_to_sort[], int start_ix, int end_ix) {
	if (start_ix < end_ix) {
		int split_ix = start_ix + (end_ix - start_ix) / 2;
		mergeSort(list_to_sort, start_ix, split_ix);
		mergeSort(list_to_sort, split_ix + 1, end_ix);
		mergeLists(list_to_sort, start_ix, split_ix + 1, end_ix);
	}
}


int main()
{
	int arr_size = 10000;
	int list_to_sort[arr_size];
	for (int f = 0; f < arr_size; f++) {
    		list_to_sort[f] = (rand() % arr_size);
	}

	//printArray(list_to_sort, arr_size);
	mergeSort(list_to_sort, 0, arr_size - 1);
	//printArray(list_to_sort, arr_size);

	return 0;
}
