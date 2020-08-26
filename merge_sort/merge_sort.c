#include <stdio.h>


void printArray(int array[], int size) {
	for ( int i = 0; i < size; i++) {
		printf("%d, ", array[i]);
	};
	printf("\n");
}


int mergeLists(int list_to_sort[], int start_a, int start_b, int end_b) {
	// copy list a to different list
	// copy list b to different list
	// iterate over both of them 
	// replace elements in list_to_sort
}


void mergeSort(int list_to_sort[], int start_ix, int end_ix) {
	if (start_ix < end_ix) {
		int split_ix = (end_ix - start_ix) / 2;
		printf("split_ix %d: \n", split_ix);
		mergeSort(list_to_sort, start_ix, split_ix);
		mergeSort(list_to_sort, split_ix + 1, end_ix);
		mergeLists(list_to_sort, start_ix, split_ix + 1, end_ix);
	}

}


int main()
{
	int list_to_sort[] = {9, 6, 5, 3, 1};
	int size = sizeof(list_to_sort)/sizeof(list_to_sort[0]);
	printf("\n %d \n", size);
	printArray(list_to_sort, size);
	mergeSort(list_to_sort, 0, size - 1);
	printArray(list_to_sort, size);

	return 0;
}
