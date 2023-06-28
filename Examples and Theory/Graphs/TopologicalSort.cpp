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



// GLOBAL VARIABLES ARE SOOO GOOOD!!!!!!!!!!
stack<ll> st;

void dfs(ll i){
    vis[i] = 1;
    for(ll x : edges[i]){
        if (!vis[x])
            dfs(x);
    }

    // after you are done with visiting a node add it to stack
    st.push(i);
    cout << "when at call stack for i: " << i << " stack is " << st.size() << "and has " << st.top() << " on top" <<"\n";
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






8 11
0 1
0 2
0 6
1 2
2 3
2 7
3 4
3 7
5 4
5 7
6 5

0 6 5 1 2 3 7 4



*/

void solve(){
    cin >> n;cin >> m;

    fi(0,m){
        cin >> u >> v;
        edges[u].pb(v);
    }

    //  PRINT YOU ADJACENCY LIST.
    fi(0,n){
        for(ll j=0;j<edges[i].size();j++)
                cout << i << "-> "<< edges[i][j] << "-> ";
        cout << "\n";
    }

    fi(0,n)
        if (!vis[i])dfs(i);
    
    cout << "\n";
    while(!st.empty()){
        cout << st.top() << " ";
        st.pop();
    }

}



int main(){
    solve();
}