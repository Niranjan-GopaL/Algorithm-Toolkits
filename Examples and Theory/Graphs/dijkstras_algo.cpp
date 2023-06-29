#include <bits/stdc++.h>
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
vector<ll> dist(arr_template_size,INT_MAX);


vector<ll> dijkstra(ll n,ll src){

    priority_queue<          
        pair<ll,ll>,        
        vector<pair<ll,ll>>,
        greater<pair<ll,ll>>
    > pq;

    dist[src] = 0;
    pq.push({0,src});

    while(!pq.empty()){
        ll dis = pq.top().first;
        ll x  = pq.top().second;
        pq.pop();

        for (ll y : edges[x]){

        }



    }


}


void solve(){

}