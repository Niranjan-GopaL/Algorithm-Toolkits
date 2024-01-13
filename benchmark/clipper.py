import pyautogui as p
import time

time.sleep(7)
p.typewrite(
'''
ll parent_[arr_template_size];
ll size_[arr_template_size];
ll rank[arr_template_size];

void make_optimized(ll v){
parent[v]=v;
size_[v]=1;
}


ll find_optimized(ll v){
if (parent[v]==v)return v;

// ------ PATH COMPRESSION -------
// otpimized , now all the nodes along 
// the path will point to the same parent
// this decreses the entire path to a depth of 1 !!!!!
return parent_[v] = find_optimized(parent_[v]);
}


ll union_by_size(ll a, ll b){
a = find_optimized(a); b = find_optimized(b);
if (a!=b){

// OPTIMIZED. now we can be sure that we'll 
// only join the smaller tree to bigger tree
if (size_[a]<size_[b])swap(a,b); 

parent_[b]=a;
size_[a] = size_[b] = size_[a]+size_[b];
}
}



                    int main(){
                                    cin >> n >> k;
                                    for(int i=0; i<n; i++)make(i);

                                    while(k--){
                                    cin >> u >> v;
                                    union1(u,v);
                                    union_by_size(u,v);
                                }

                    ll connected_ct = 0;
                    for (int i=0; i<n; i++) 
                    if (find_optimized(i) == i)
                    connected_ct++;

                    cout << connected_ct << endl;
                }
'''
)
p.typewrite(['enter'])
