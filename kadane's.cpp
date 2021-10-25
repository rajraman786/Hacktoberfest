#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    int bsum=0;
    int sum=0;
    for(int i=0;i<n;i++)
    {
        if(arr[i]+sum>=arr[i])
        {
            sum+=arr[i];
            if(sum>bsum)
                bsum=sum;
        }
        else
        {
            sum=arr[i];
        }

    }
    cout<<bsum;
    return 0;
}