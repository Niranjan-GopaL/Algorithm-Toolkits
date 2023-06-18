#include <bits/stdc++.h>
#include <iostream>

using namespace std;

#define ll long long int


int PrefixSum(int BIT[], int i)
{
	int sum = 0; // Iniialise sum 
	while (i>0)
	{
		sum += BIT[i];
		i -= i & (-i);
	}
	return sum;
}


void updateBIT(int BIT[], int n, int i, int X)
{
	while (i <= n)
	{
		BIT[i] += X;
		i += i & (-i);
	}
}


// This is the contructor sir gave that works in O(nlogn)
// It calls updateBIT for each element of input array
int* constructBIT(int A[], int n)
{
	int *BIT = new int[n+1];
	for (int i=1; i<=n; i++)
		BIT[i] = 0;
	for (int i=1; i<=n; i++)
		updateBIT(BIT, n, i, A[i]);
	return BIT;
}


// Linear Time algorithm
// KEY IDEA:- 
//   i) copy inp arr as BIT
//  ii) add curr elem to IMMEDIATE PARENT of elem 
int* makeBIT(int A[], int n)
{
    int *BIT = new int[n+1];
    for (int i=1; i<=n; i++)
		BIT[i] = A[i-1];

    for (int  i = 0; i < n; i++)
    {
        // p is the immediate parent of the element
        int p = i + i & -i;
        if (p<=n)
            // updateing parent to incorporate current elem
            BIT[p] = BIT[p] + BIT[i];
    }
    
    return BIT;
}

int main() {
    int A[50000], n, l, r, i, k;
	cin >> n;

	// filling first n elements with ran
	for (i = 0; i < n; ++i)
        A[i] = rand () % 4 * n + i; // <-- why rand filling?
	
	for (int i = 1; i <= n; ++i)
		A[i] = 200 - rand () % 100;
	
	int *BIT = constructBIT(A, n);
	cout << " Inpute for PrefixSum";
	cin >>i;
	cout << "PrefixSum "<<i<<"is"<< PrefixSum(BIT, i);
		
	cout << " Inpute for Update";
	cin >>l>>k;
	A[l]+=k;
	updateBIT(BIT, n, l, k); 
		
	cout << "PrefixSum "<<i<<"is"<< PrefixSum(BIT, i);

	return 0;

}