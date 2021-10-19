#include<bits/stdc++.h>
#include<iostream>

using namespace std;

void rearrange(int arr[],int n)
{
    int j=0;
    for(int i=0;i<n;i++)
    {
        if(arr[i]<0)
        {
            if(i!=j)
            {
                swap(arr[i],arr[j]);
                j++;
            }
        }
    }
}
void printarray(int arr[],int n)
{
    for(int i=0;i<n;i++)
    {
        cout<< arr[i] << " ";
    }
}
int main()
{
    cout<<"enter the no of test cases"<<endl;
    int t;
    cin>>t;
    while(t--)
    {
        int arr[100];
        cout<<"enter the size of array"<<endl;
        int n;
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        rearrange(arr,n);
        
        cout<<"RESULT"<<endl;
        
        printarray(arr,n);
    }
    return 0;
}    