/// MY ATTEMPT TO GET INTO CPP

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

/// @brief builds a BINARY TREE
/// @param vec : the vector of values that is level order traversal of the tree to be constructed
/// @param n : size of the vector
/// @return root of the tree built
node* build_tree(vector<int> vec,int n){
    if (n == 0) return NULL;

    queue<node*> q;
    node *root = new node(vec[0]);
    q.push(root);

    int i = 1;
    while(!q.empty()){
        node *temp = q.front();
        q.pop();

        
        if (i<n){
            temp -> l = new node(vec[i]);
            q.push(temp->l);
        }
        i++;

        if (i<n){
            temp -> r = new node(vec[i]);
            q.push(temp->r);
        }
        i++;

    }
    return root;
}


/// @brief checks if it is BINARY SEARCH TREE, i.e if it satisfies the SEARCH PROPERTY OF BST 
/// @param node 
/// @param min 
/// @param max 
/// @return bool
bool is_BST(node* node,int min, int max){
    if (node == NULL) return 1;
    if (node->val < min || node->val > max) return 0;
    return is_BST(node->l,min,node->val) && is_BST(node->r,node->val,max); 
}

int main(){
    int n; cin >> n ;vector<int> vec;int val;

    while(n){
        cin >> val;
        vec.push_back(val);
        n--;
    }

    node* root = build_tree(vec,vec.size());

    if (is_BST(root,INT_MIN,INT_MAX)) cout << root->val <<" YES";
    else cout << root->val << " NO";
}