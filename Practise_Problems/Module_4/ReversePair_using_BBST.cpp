#include<bits/stdc++.h>
using namespace std;

#define ll long long int

class node{
    public:
    ll data;
    ll num;
    node* left;
    node* right;
    node(ll d){
        this->data = d;
        this->num = 0;
        this->left = NULL;
        this->right =NULL;
    }
};


ll Num(node* root){

    if(root==NULL) return 0;    
    else return root->num;

}


node* insert2(node* root, ll data){

    if(root==NULL) root = new node(data);
    
    else if (data <= root->data) root->left = insert2(root->left,data);
    
    else insert2(root->right,data);
    
    root->num = 1+Num(root->left)+Num(root->right);
    return root;
}



ll find_rank(node*root, ll x){
    ll r = 0;

    while (root){
    if(root->data==x) {
        r = r+Num(root->right);
        return r;
    }
    else if (root->data<x){
        root = root->right;
    }
    else {
        r = r+1+Num(root->right);
        root = root->left;
    }
    }
    return r;
}

int main() {
    ll n,val,total,target;
    cin>>n;
    vector<ll>vec ;
    total = 0;
    node* root1 = NULL;
    node* root2 = NULL;
    ll z = 0;
    for (ll  i = 0;i<n;i++){
        cin>>val;
        vec.push_back(val);
        z = find_rank (root1, 2*val);
        root1 = insert2(root1,val);
        total = total + z;
    }
    
    cout<<total;
}