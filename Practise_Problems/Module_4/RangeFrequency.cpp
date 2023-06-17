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

};


int main(){
    return 0;
}