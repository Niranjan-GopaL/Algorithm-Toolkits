#include <bits/stdc++.h>
using namespace std;

#define ll                   long long
#define fo(a,b)              for(ll i=a; i<b; i++)
#define pb                   push_back




// global stuff will be initialized fine
ll n,m,k,q,x,y,z;
ll u,v;
const ll arr_template_size = 1e6;

// global int   arrays are initialized to 0
ll a[arr_template_size];
ll b[arr_template_size];
ll c[arr_template_size];
vector<ll> edges[arr_template_size];


string s,t;
ll ans;


ll labels[arr_template_size];   // current component of each vertex
ll nedges[arr_template_size];   // number of edges in each component
ll sz[arr_template_size];       // size of each component



// relabel vertex v and neighbors to label "target"
void relabel(ll v, ll target){ 

    if (labels[v] == target) return;

    labels[v] = target;

    for(ll x : edges[v])
        labels[x] = target;
}


void merge(ll u, ll v){

    edges[u].pb(v);
    edges[v].pb(u);

    ll cu = labels[u]; ll cv = labels[v];

    // NICEEE !!!!!!!
    // arbitarily picking cu and increasing its
    // number of edges. cuz when we merge two component
    // (Think of just two nodes) 

    // the number of edges of the merged component isn't just 
    // sum of the edges of the two components but its 
    // 1 + sum of the edges in each component
    ++nedges[cu]; 

    if (cu == cv) return;

    if (sz[u] > sz[v] ){
        swap(u,v);
        swap(cu,cv);
    }


    // so we are sure that we merge shorter 
    // component to the larger one
    relabel(u,cv);

    sz[cv] += sz[cu];
    nedges[cv] += nedges[cu];
}


void solve(){
    cin >> n >> m;

    fo(0,n)sz[i]=1;
    fo(0,n)labels[i]=i;


    fo(0,m)
    {
        cin >> u >> v;
        u--;v--;
        merge(u,v);
    }

    bool possible = 1;

    fo(0,n){
        // if size of components is not n*(n-1)/2 n=number of edges
        // there exist a pair that is not "paired" hence the 
        // graph is not REASONABLE.
        if (nedges[labels[i]] != sz[labels[i]]*(sz[labels[i]]-1)/2){
            possible = 1;
            break;
        }
    }

    cout << (possible ? "YES\n" : "NO\n");
}



int main(){
    solve();
}




/*



5 3
0 1
1 2
0 2

YES



5 3
0 1
1 2
1 3

NO


*/

