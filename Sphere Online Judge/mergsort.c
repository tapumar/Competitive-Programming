#include <stdio.h>

void merge(int left[],int l,int right[],int r,int A[])
{
	int i, j, k;
	i = j = k = 0;
	while (i < l && j < r) {
		if (left[i] <= right[j]) {
			A[k] = left[i];
			i++;
		} else {
			A[k] = right[j];
			j++;
		}
		k++;
	}
	while (i < l) {
		A[k] = left[i];
		i++;
		k++;
	}
	while (j < r) {
		A[k] = right[j];
		j++;
		k++;
	}
}

void merge_sort(int A[], int n)
{
	int i, j, mid;
	if (n < 2) {
		return;
	}
	mid = n / 2;
	int left[mid];
	int right[n - mid];
	for(i = 0; i < mid; i++) {
		left[i] = A[i];
	}
	for(i = mid; i < n; i++) {
		right[i - mid] = A[i];
	}
	merge_sort(left,mid);
	merge_sort(right,n - mid);
	merge(left,mid,right,n-mid,A);
}

int main()
{
	int A[100000], c = 0, i;
	while(scanf("%d", &A[c]) != EOF) {
		c++;
	}
	merge_sort(A,c);
	for(i = 0; i < c; i++) {
		printf("%d ", A[i]);
	}
	printf("\n");
	return 0;
}
