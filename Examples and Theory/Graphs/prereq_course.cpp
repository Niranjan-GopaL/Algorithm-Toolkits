#include <bits/stdc++.h>
using namespace std;

#define ll long long int

ll n,m,q,t;
ll u,v;
vector<ll> edges[10005];
bool vis[10005];
ll a[10005];



/* Aditya's test case
4
4
0 1 1 2 0 3 3 2
6
0 2 0 3 3 1 3 2 2 3 2 0



*/

bool dfs(ll i,ll b,ll pos){
    if (vis[i])return 0;

    vis[i]=1;
    for(ll x : edges[i]){
        if (!vis[x]){
            if (x == b)return 1;
            
            pos = dfs(x,b,pos);
        }
    }
    return pos;
}


bool bfs(ll i,ll b){
    queue<ll> q; q.push(i);

    while(!q.empty()){
        ll x = q.front();q.pop();

        if (vis[x])continue;
        vis[x] = 1;

        for (ll y: edges[x])
            if (!vis[y]){
                if (y == b)return 1;
                q.push(y);
            }
    }
    return 0;
}




void  solve(){
    cin >> n;
    cin >> t;
    // cout << n  << t<< endl;

    for(ll i = 0; i < t; ++i){
        cin >> u >> v;
        // cout << u << v << endl;
        edges[u].push_back(v); // directed graph
    }

    cin >> q;
    // cout << q << endl;

    ll a1,b1;
    for(ll i = 0; i < q; ++i){
        cin >> a1 >> b1;
        // for(ll j=0;j<n;++j)vis[i]=0; //below is much faster and better way to do this
        memset(vis, 0, sizeof(vis));
        // a[i]=dfs(a1,b1,0);
        a[i]=bfs(a1,b1);
    }

    for(ll i = 0;i<q; i++)
        cout << a[i] << " ";


}


int main(){
    solve();
}
/*


3
3
1 2 1 0 2 0
2
1 0 1 2

out
1 1




2
0
2
1 0 0 1

out
0 0







2
1
1 0
2
0 1 1 0

out
0 1





5
4
0 1 1 2 2 3 0 3
4
0 3 3 2 4 2 1 3



*/