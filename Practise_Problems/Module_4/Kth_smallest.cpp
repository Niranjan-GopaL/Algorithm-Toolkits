#include <bits/stdc++.h>
using namespace std;

struct node
{
    int val;
    struct node *l;
    struct node *r;

    node(int value){
        val = value;
        l = NULL;
        r = NULL;
    }
};

node* build_tree(vector<int> vec, int idx){
    if (idx >= vec.size() || vec[idx] == -1) return NULL;

    node* root = new node(vec[idx]) ;
    root->l = build_tree(vec,2*idx+1);
    root->r = build_tree(vec,2*idx+2);
    
    return root;
}


int main(){
    ;
}