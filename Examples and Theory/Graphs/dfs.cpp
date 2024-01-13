// Usual template stuff
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

#define ll             long long
#define fi(a,b)        for(ll i=a; i<b; i++)
#define fj(a,b)        for(ll j=a; j<b; j++)
#define pb             push_back


// global stuff will be initialized fine
ll n,m,k,q,x,y,z;
ll u,v;
const ll arr_template_size = 1e6;

// global int   arrays are initialized to 0
ll a[arr_template_size];
ll b[arr_template_size];
ll c[arr_template_size];

string s,t;
ll ans;


vector<ll> edges[arr_template_size];
bool vis[arr_template_size];



ll discovery_time[arr_template_size];
ll finish_time[arr_template_size];
ll phi[arr_template_size];
ll cnt = 0;

void dfs(){
    vis[u] = 1;discovery_time[u]=cnt++;
}




void solve(){

    fi(0,n){
        cin >> u >> v;
        // array of vectors 
        edges[u].pb(v);
        edges[v].pb(u);
    }

    //  PRINT YOU ADJACENCY LIST.
    fi(0,n){
        for(ll j=0;j<edges[i].size();j++)
                cout << i << "-> "<< edges[i][j] << "-> ";
        cout << "\n";
    }



    fi(0,arr_template_size)phi[i]=-2;

}