#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define go(i,a,b) for(ll i=a; i<=b; i++)
#define pb push_back 


ll n,m,q,t;
ll u,v;
vector<ll> edges[10005];
bool vis[10005];
ll a[10005];


int main(){

    go(i,0,n){
        cin >> u >> v;
        edges[u].pb(v);
        edges[v].pb(u);
    }
}