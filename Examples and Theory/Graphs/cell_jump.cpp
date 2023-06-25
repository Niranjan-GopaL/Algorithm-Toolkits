#include <bits/stdc++.h>
#include <iostream>
using namespace std;

#define ll long long int


// global stuff will be initialized fine
ll n,m,k,q,x,y,z;
const ll arr_template_size = 1e6 + 8432;

// global int   arrays are initialized to 0
ll a[arr_template_size];
ll b[arr_template_size];
ll c[arr_template_size];

string s,t;
ll ans;



void solve(){
    ll t;
    cin >> n >> t;
    
    for(ll i=0; i<n-1; i++)cin >> a[i];

    ll cur = 0;
    do
    {
        if (cur == t) {
            cout << "YES";
            return;
        }
        cur += a[cur];
    } while (cur < n);

    cout << "NO";
    return;  
}


int main(){
    solve();
}