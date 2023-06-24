#include <bits/stdc++.h>
#include <iostream>
using namespace std;

#define ll long long


// global stuff will be initialized fine
ll n,m,k,q,x,y,z;
ll u,v;
const ll arr_template_size = 1e6 + 8432;

// global int   arrays are initialized to 0
ll a[arr_template_size];
ll b[arr_template_size];
ll c[arr_template_size];

string s,t;
ll ans;


vector<ll> edges[10005]; // ARRAY OF VECTORS
bool vis[10005]; // and not THIS --->   vector<bool> vis[10005]
 

void solve(){
    cin >> n >> m;

    // m lines each start with 'k' and the k numbers are given who are friends
    for(ll i=0; i < m; i++){
        ll k; cin >> k;

        for(ll j=0; j+1 <k; j++){
            cin >> u >> v;
            u--;v--;
            edges[u].push_back(v);
            edges[v].push_back(u);
        }
    }

    for(ll i;i<n;i++){
        for(ll j;j<edges[i].size();j++)
                cout << edges[i][j] << "-> ";
        cout << "\n";
    }

    for(ll i=0;i<n;i++){

        if( !vis[i] ){
            vector<ll> cluster;
            queue<ll> q;
            q.push(i);

            // the queue will be empty only when all nodes in cluster is visited exactly once
            while(!q.empty()){
                ll x = q.front();
                q.pop();

                if ( !vis[i] ) continue; // if the node was visited already go to the next node in queue
                vis[i] = 1; 
                cluster.push_back(x);

                // pushing all the adjacent nodes to the queue
                for (ll adjacent : edges[x])
                    if (!vis[adjacent])
                        q.push(adjacent);
                
            }

            
            // answer array will mark all nodes with the size of the cluster that they are part of
            for(ll node : cluster){
                
                a[node] = cluster.size();
            }

        }
    }


    // answer array has size of the cluster that it is a part of
    for (ll i = 0; i < n; i++)
        cout << a[i] << " ";
}



int main(){
    solve();
}