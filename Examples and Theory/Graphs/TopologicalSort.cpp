#include <bits/stdc++.h>
using namespace std;

#define ll              long long
#define fi(a,b)        for(ll i=a; i<b; i++)
#define fj(a,b)        for(ll j=a; j<b; j++)
#define pb              push_back


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




stack<ll> st;
void dfs(ll i){

    vis[i] = 1;
    for(ll x : edges[i]){
        if (!vis[i])
            dfs(x);
    }
    st.push(i);
}

/*
6
5 0
5 2
2 3
3 1
4 0
4 1


0:
1:
2:3
3:1
4:0,1
5:0,2

*/

void solve(){
    cin >> n;

    fi(0,n){
        cin >> u >> v;
        edges[u].pb(v);
    }

    fi(0,n)
        if (!vis[i])dfs(i);
    

    while(!st.empty()){
        cout << st.top() << " ";
        st.pop();
    }
}



int main(){
    solve();
}