#include <iostream>
#include <algorithm>
#define MAX 9
using namespace std;
int n,m;
int arr[MAX];
int givenArr[MAX];
void dfs(int num, int k)
{
    if(k==m)
    {
        for(auto i=0; i<m; i++)
            cout<<arr[i]<<" ";
        cout<<endl;
    }
    else{
        for(auto i=0; i<n; i++)
        {
            bool temp = true;
            for(auto j=0; j<k; j++)
            {
                if(arr[j]==givenArr[i]){
                    temp = false;
                }
            }
            if(temp){                
                arr[k] = givenArr[i];
                dfs(i,k+1);
            }
        }
    }
}

int main()
{
    cin>>n>>m;
    for(auto i = 0; i<n; i++){
        cin>>givenArr[i];
    }
    sort(givenArr,givenArr+n);
    dfs(0,0);
}