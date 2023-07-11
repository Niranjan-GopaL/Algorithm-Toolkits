#include <bits/stdc++.h>
using namespace std;

#define ll             long long
#define fi(a,b)        for(ll i=a; i<b; i++)
#define fj(a,b)        for(ll j=a; j<b; j++)
#define pb             push_back


// global stuff will be initialized fine
ll n,m,k,q,x,y,z,s;
ll u,v;
const ll arr_template_size = 1e6;

// global int   arrays are initialized to 0
ll a[arr_template_size];

vector<ll> adj[arr_template_size];
ll sweets[arr_template_size];

ll bfs(ll d, ll s){
    int vis[n]={0};
    queue<pair <ll,ll>> q;

    q.push({s, sweets [s]});
    vis[s] = 1; ll ans = INT_MAX;

    while (!q.empty()) {
        ll u = q.front().first; ll v = q.front().second; q.pop();

        for (ll i : adj[u]){
            if (!vis[i]){
                q.push({i, (ll) max(v, sweets[i])}); 
                vis[i] = 1;
            }

            if ( i ==d)
                ans = min(ans, (ll) max(v, sweets[i]));
        }
    }
    return ans;
}


/* TEST CASE



3 4 1
3 4 5
1 2
1 3
2 3
3 2

OUTPUT !!!!
3 4 5 




4 5 2
6 3 2 5
2 1
2 4
1 3
4 3
3 1

OUTPUT !!!!
6 3 5 5 


*/

int main(){

    cin >> n >> m >> s ;
    fi(0,n)
        cin >> sweets[i];
    
    fi(0,m){
        cin >> u >> v;
        adj[u--].pb(v--);
    }

    fi(0,n){
        if (i == s-1)
            cout << sweets[i] << " ";
        else
            cout << bfs(i, s-1) << " ";
    }

    return 0;
}