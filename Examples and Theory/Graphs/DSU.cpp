#include <bits/stdc++.h>
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




// THIS IS THE BASIC OVERVIEW OF ALL THE IMPRTANT STUFF

ll parent[arr_template_size];

void make(ll v){
    parent[v]=v;
}

ll find(ll v){
    if (parent[v]==v)return v;
    return find(parent[v]);
}

ll union1(ll a, ll b){
    a = find(a); b = find(b);
    if (a!=b)parent[b]=a;
}

// create a union function in a DSU that uses union by rank




// BUT FURTHUR OPTIMIZATION IS POSSIBLE

// union by rank ----> when we union two sets we union based on rank
// union by size ----> when we union two sets we union based on size
// path compression ----> this is the inverse ackerman function Time complexity


ll parent_[arr_template_size];
ll size_[arr_template_size];
ll rank[arr_template_size];

void make_optimized(ll v){
    parent[v]=v;
    size_[v]=1;
}


ll find_optimized(ll v){
    if (parent[v]==v)return v;

    // ------ PATH COMPRESSION -------
    // otpimized , now all the nodes along 
    // the path will point to the same parent
    // this decreses the entire path to a depth of 1 !!!!!
    return parent_[v] = find_optimized(parent_[v]);
}


ll union_by_size(ll a, ll b){
    a = find_optimized(a); b = find_optimized(b);
    if (a!=b){

        // OPTIMIZED. now we can be sure that we'll 
        // only join the smaller tree to bigger tree
        if (size_[a]<size_[b])swap(a,b); 

        parent_[b]=a;
        size_[a] = size_[b] = size_[a]+size_[b];
    }
}
                


int main(){
    cin >> n >> k;
    for(int i=0; i<n; i++)make(i);

    while(k--){
        cin >> u >> v;
        union1(u,v);
        union_by_size(u,v);
    }

    ll connected_ct = 0;
    for (int i=0; i<n; i++) 
        if (find_optimized(i) == i)
            connected_ct++;

    cout << connected_ct << endl;
}