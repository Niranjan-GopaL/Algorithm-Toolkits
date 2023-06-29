// Dikjstra's fails for negetive cycle
// It also fails for negetive edge weight

// This algorithm detects negetive cycle [only in DG]
// It works fine for negetive edge weight

// If we need to work in undirected graph then we need to 
// modify it so that  A ---- B :W is implemented as 
// A ----> B :W and B ----> A :W (both same weight) THAT'S IT !!!!

#include <bits/stdc++.h>
using namespace std;

#define ll             long long
#define fi(a,b)        for(ll i=a; i<b; i++)
#define fj(a,b)        for(ll j=a; j<b; j++)
#define pb             push_back


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


 