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

        
        if (i<n){
            temp -> lc = new node(vec[i]);
            q.push(temp->lc);
        }
        i++;

        if (i<n){
            temp -> rc = new node(vec[i]);
            q.push(temp->rc);
        }
        i++;

    }
    return root;
}

bool is_BST(node* node,int min, int max){
    if (node == NULL) return 1;
    if (node->data < min || node->data > max) return 0;
    return is_BST(node->lc,min,node->data) && is_BST(node->rc,node->data,max); 
}

int main(){
    int n; cin >> n ;vector<int> vec;int val;

    while(n){
        cin >> val;
        vec.push_back(val);
        n--;
    }

    node* root = build_tree(vec,1,vec.size());

    if (is_BST(root,INT_MIN,INT_MAX)) cout << root->data <<" YES";
    else cout << root->data << " NO";
}