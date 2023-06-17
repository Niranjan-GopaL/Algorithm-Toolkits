#include <bits/stdc++.h>
using namespace std;

struct node
{
    int data;
    struct node *lc;
    struct node *rc;

    node(int val){
        data = val;
        lc = NULL;
        rc = NULL;
    }
};

node* build_tree(vector<int> vec, int i,int n){
    if (n == 0) return NULL;

    queue<node*> q;
    node *root = new node(vec[0]);
    q.push(root);

    while(!q.empty()){
        node *temp = q.front();
        q.pop();

        
    }
}
