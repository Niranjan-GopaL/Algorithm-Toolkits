#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define fi(i,a,b) for(ll i=a; i<b; i++)
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


ll dfs(ll i, ll c){

    if (vis[i]) return c;

    vis[i] = 1;c = 1;

    for (ll x : edges[i])
        if (!vis[x]){
            c += dfs(x,c);
        }

    return c;
}

/* TEST CASES

4 1
0 2


*/


int main(){
    cin >> n >> m;
    fi(i,0,m){
        cin >> u >> v;
        edges[u].pb(v);
    }

    ll cmpt;
    vector<ll> nodes;
    fi(i,0,n){
        if (!vis[i]){
            nodes.pb(dfs(i,0));
            cmpt++;
        }
    }

    ll nc2 = n*(n-1)/2;

    for (ll num : nodes)
        nc2 -= num*(num-1)/2;
    
    cout << nc2 << endl;
}