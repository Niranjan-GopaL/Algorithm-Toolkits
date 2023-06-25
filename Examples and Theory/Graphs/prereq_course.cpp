#include <bits/stdc++.h>
using namespace std;

#define ll long long int

ll n,m,q,t;
ll u,v;
vector<ll> edges[10005];
bool vis[10005];


int dfs(i,b,pos){
    if (vis[i])return 0;

    for(x : edges[i]){
        if (!vis[x]){
            if (x == b)return 1;
            
            vis[x] = 1;
            pos = dfs(x,b,pos);
        }
    }
    return pos;
}



void  solve(){
    cin >> n;
    cin >> t;
    for(ll i = 0; i < t/2; ++i){
        cin >> u >> v;
        edges[u].push_back(v); // directed graph
    }

    cin >> q;
    for(ll i = 0; i < q/2; ++i){
        cin > a >> b;
        dfs(a,b)
    }


}


int main(){
    solve();
}