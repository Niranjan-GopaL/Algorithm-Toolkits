//  find median of a matrix
#include<bits/stdc++.h>
using namespace std;

#define ll long long

const int MAX = 100;

int binaryMedian(ll** m, ll r ,ll c)
{
	ll min = INT_MAX, max = INT_MIN;
	for (ll i=0; i<r; i++)
	{
		if (m[i][0] < min)
			min = m[i][0];
		if (m[i][c-1] > max)
			max = m[i][c-1];
	}

	ll desired = (r * c + 1) / 2;
	while (min < max)
	{
		ll mid = min + (max - min) / 2;
		ll place = 0;
		for (ll i = 0; i < r; ++i)
			place += upper_bound(m[i], m[i]+c, mid) - m[i];
		if (place < desired)
			min = mid + 1;
		else
			max = mid;
	}
	return min;
}

int main()
{
	ll R, C;
    cin >> R >> C;
    
	ll **arr = new ll*[R];
    for (ll i = 0; i < R; i++) {
        arr[i] = new ll[C];
    }

    for (ll i = 0; i < R; i++) {
        for (ll j = 0; j < C; j++) {
            cin >> arr[i][j];
        }
    }

	cout << "Median is " << binaryMedian(arr, R, C) << endl;
}
