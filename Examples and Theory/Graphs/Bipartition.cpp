#include <bits/stdc++.h>
#include <algorithm>
using namespace std;


#define ll long long

// global stuff will be initialized fine
ll n,m,u,v;



vector<ll> edges[10005];
bool vis[10005];
bool col[10005];

bool possible= 1;


void dfs(ll i,bool color){
    if(vis[i]) return;
    
    vis[i]=1;
    col[i]=color;

    for(ll next : edges[i]){
        if (!vis[next] ){
            // logical xor is a trick to make it the other color, 
            // in this case it's same as !color
            dfs(next,color^1); 
        }else{
            if(col[next] == color)possible = 0;
        }
    }
     
}

void solve(){
    cin >> n >> m;

/* 


3 3

1 2
2 3
1 3

0-> 1-> 0-> 2->
1-> 0-> 1-> 2->
2-> 1-> 2-> 0->

THIS ISN'T A PROBLEM HERE, BUT IT WILL BE IN FUTURE.

*/


    for(ll i=0;i<m;i++){
        cin >> u >> v;  
        u--;v--;
        edges[u].push_back(v);
        edges[v].push_back(u);
    }

    for(ll i=0;i<n;i++){
        for(ll j=0;j<edges[i].size();j++)
                cout << i << "-> "<< edges[i][j] << "-> ";
        cout << "\n";
    }


    for(ll i=0;i<n;i++)
        if(!vis[i])
            // so we color the starting edge of all clusters with 0 
            dfs(i,0);



    if (possible){


        // THIS IS THE NEWWW SUPERPOWERRRR!!!!!!!!! 
        ll cnt[2] = {0}; // initializes all elements of array to 0
        for(ll i=0;i<n;i++)++cnt[col[i]];

        // how many are colored 0
        cout << col[0] << "\n";
        for(ll i=0;i<n;i++)
            if (col[i]==0)
                cout << i+1 << " ";
        cout << "\n";



        // how many are colored 1
        cout << col[1] << "\n";
        for(ll i=0;i<n;i++)
            if (col[i]==1)
                cout << i+1 << " ";
        cout << "\n";
    }else{
        cout << -1<<"\n";
    }
    

}






int main(){
    solve();
}