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


// BUT FURTHUR OPTIMIZATION IS POSSIBLE

// union by rank
// union by size
// path compression