import pyautogui as p
import time

time.sleep(7)
p.typewrite(
'''

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

'''
)
p.typewrite(['enter'])
