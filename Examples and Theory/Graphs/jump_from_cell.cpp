#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define go(i,a,b) for(ll i=a; i<b; i++)
#define pb push_back 


const ll arr_template_size = 1e6 + 8432;

ll n,m,q,t;
ll u,v;

// global int   arrays are initialized to 0
vector<ll> edges[arr_template_size];
bool vis[arr_template_size];
ll a[arr_template_size];
ll b[arr_template_size];
ll c[arr_template_size];



/*

5 
3 0 2 1 2
2

0
W


7
4 2 3 0 3 1 2
0

1
W


7
4 2 3 0 3 1 2
5

1
W


*/


void solve(){
    cin >> n;
    go(i,0,n)cin >> a[i];
    cin >> m;
    int pos = 0;

    // push index to a queue
    queue<ll> q;q.push(m);

    while(!q.empty()){
        // get index from queue
        ll x = q.front();q.pop();

        if (vis[x])continue;
        vis[x] = 1;

        if (a[x] == 0){
            pos = 1;
            break;
        }

        if (x + a[x] < n)q.push(x + a[x]); 
        if (x - a[x] > -1)q.push(x - a[x]); 
    }

    cout << pos;
}




int  main(){
    solve();
}