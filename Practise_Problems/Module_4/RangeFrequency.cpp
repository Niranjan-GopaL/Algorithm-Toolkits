#include  <bits/stdc++.h>
using namespace std;

class RangeFrequency{
    public:
    int n,x;int *A,*ST;
    RangeFrequency(int n1,int A1[]){
        n = n1;
        x = (int)((ceil)(log2(n)));
        A = new int[n];
        for (int i = 0; i < n; i++)
            A[i] = A1[i];
        ST = new int[(int)(2*pow(2,x)-1)];
    }

    void making_ST(int val){
        int z = 2*pow(2,x) - 1;
        for (int i = (z/2+n); i < z; i++)
            ST[i] = 0;

        for (int i = 0; i < n; i++)
        {
            if (A[i] == val) ST[z/2+i] = 1;
            else  ST[z/2+i] = 0;
        }

        for (int i=z/2-1; i>-1; i--)
            ST[i] = ST[2*i+1] + ST[2*i+2];
    }

    int RangeQuery(int i,int ss,int se,int l,int r){
        if (ss>=l and se <= r) return ST[i];
        if (se<l or ss>r) return -1;

        int mid = ss + (se-ss)/2;
        int m1 = RangeQuery(2*i+1,ss,mid,l,r);
        int m2 = RangeQuery(2*i+2,mid+1,se,l,r);

        if (m1<0) return m2;
        else if(m2<0) return m1;
        else return m1+m2;
    }

};


int main(){
    int n;cin >> n;int A[n];
    for (int  i = 0; i < n; i++)
        cin >> A[i];

    int m;cin >> m;
    int l,r,val;

    RangeFrequency obj =  RangeFrequency(n,A);

    int ans[m];int k = 0;
    while(k<m){
        cin >> l >> r >> val;
        obj.making_ST(val);
        if(!(l>=0 and r>=l and n>r)){
            ans[k++] = -1;
            continue;
        }

        int x = (int)((ceil)(log2(n)));
        ans[k++] = obj.RangeQuery(0,0,pow(2,x)-1,l,r);
    }

    for(int i=0;i<m;i++)
        cout << ans[i] << " ";
}