#include <iostream>
#define MAX 9
using namespace std;
int n,m;    
int arr[MAX];
void dfs(int num, int k)
{
    if(k==m){
        for(auto i = 0; i<m; i++)
        {
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }
    else{
        for(auto i = num; i<=n; i++)
        {
            arr[k] = i;
            dfs(i,k+1);
        }
    }
}

int main()
{
    cin>>n>>m;
    dfs(1,0);
}