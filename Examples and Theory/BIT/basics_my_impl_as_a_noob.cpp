#include <bits/stdc++.h>
using namespace std;

int Prefix_SUM(int idx,vector<int> vec){
    int sum_ = 0;
    while(idx){
        sum_ = sum_ + vec[idx];
        idx -= idx & -idx;
    }
    return sum_;
}

vector<int> update(int idx, int increase,vector<int> BIT){
    while (idx < BIT.size())
    {
        BIT[idx] += increase;
        idx += idx & -idx;
    }
    return BIT;
}

int main(){

    int n; cin >> n ;vector<int> vec;int val;
    while(n){
        cin >> val;
        vec.push_back(val);
        n--;
    }

    // prints the inputed vector
    for (int i = 0; i < vec.size(); i++)
        cout << vec[i] << endl;

    // Inserting into the vector
    // the working of this impl is pretty fked up
    // turns out even if a function modifies vector it woun't be affected.
    // so I had to write this complicated working shitty function.
    // IT WORKS BUT IS TERRIBLE
    vector<int> BIT(vec.size()+1,0);
    for (int i=1; i < vec.size()+1; i++)        
         BIT = update(i,vec[i-1],BIT);

    // Prints the BIT
    for (int i = 1; i < vec.size()+1; i++)
        cout << BIT[i] << " ";

    int idx; cin >> idx;
    cout << " Prefix sum for the idx " << idx << " is" << Prefix_SUM(idx,BIT) << endl;

}