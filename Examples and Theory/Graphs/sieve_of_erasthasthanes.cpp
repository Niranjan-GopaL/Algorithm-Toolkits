#include <bits/stdc++.h>
using namespace std;

#define ll             long long
#define fi(a,b)        for(ll i=a; i<b; i++)
#define fj(a,b)        for(ll j=a; j<b; j++)
#define pb             push_back
/*





*/

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



bool is_prime(ll n){
    fi(2,sqrt(n)+1)
        if (n%i==0) return false;
    
    return true;
}


void naive_way(ll n){
    fi(2,n+1)
        if (is_prime(i))
            cout << i << " ";
}


void sieve(ll n){

    vector<bool> is_prime(n+1, true);


    fi(2,int(sqrt(n))+1)
    {
        if (is_prime[i])

            // MUCHH MORE EFFICIENT 
            for(ll j=i*i; j<=n; j+=i)is_prime[j] = false;  

            // this is easier to understand. we replace 
            // j=2*i (here we simply put already made true numbers as true)  
            // with j=i^2 (NO DOUBLE COUNTING !!! )
            // for(ll j=2*i; j<=n; j+=i)is_prime[j] = false;  
         
    }

    fi(2,n+1)
        if (is_prime[i])
            cout << i << " ";

}

int main(){
    cin >> n;
    cout << "Sieve way" << endl;
    sieve(n);
    cout << endl;

    // cout << "naive way" << endl;
    // naive_way(n);
}