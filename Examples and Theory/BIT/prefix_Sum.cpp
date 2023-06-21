#include <bits/stdc++.h>
#include <iostream>

using namespace std;

// Such a nice algorithm
// sweet O(1)
int* prefix_sum(int* arr,int n){
    int* prefix_sum = new int[n];

    prefix_sum[0] = arr[0];
    for(int i=1;i<n;i++)
        prefix_sum[i] = prefix_sum[i-1] + arr[i];

    return prefix_sum;
}



int main(){
    int n;cin >> n;
    int* A = new int[n];
    for(int i = 0; i < n;i++)
        cin >> A[i];
    int* prefix_sum_A = prefix_sum(A,n);

    for(int i = 0; i < n; i++)
        cout << prefix_sum_A[i] << endl;
}