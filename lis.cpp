// Largest increasing subsequence
#include <iostream>
#include <cstdio>
using namespace std;

int lcs(int a[], int n)
{
	int *lis, max, i, j;
	lis = new int[n];
	max = 0;
	for (i = 0; i < n; i++) {
		lis[i] = 1;
	}

	for (i = 1; i < n; i++)
	{
		for (j = 0; j < i; j++) {
			if (a[i] > a[j] && lis[i] < lis[j] +1) {
				lis[i] = lis[j] +1;
			}
		}
	}
	for (i=0; i<n;i++)
	{
		cout<<lis[i]<<endl;
	}
	for (i = 0; i < n; i++) {
		if (max < lis[i]) {
			max = lis[i];
		}
	}
	return max;
}

int main()
{
	int arr[] = { 10, 22, 9, 33, 21, 50, 41, 60 };
  	int n = sizeof(arr)/sizeof(arr[0]);
  	printf("Length of LIS is %d\n", lcs( arr, n ) );
	return 0;
}