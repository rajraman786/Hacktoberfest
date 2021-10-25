#include<iostream>
using namespace std;

class Edge{
    public:
    int source;
    int dest;
    int weight;
};
void bellman_ford(Edge *input,int n,int e,int s)
{
    int weight[n+1];
    for(int i=0;i<n;i++)
        weight[i]=INT_MAX;
    weight[s]=0;
    for(int i=0;i<n;i++)
        {
            cout<<weight[i]<<"  ";
        }
    cout<<endl;
    for(int pass=0;pass<n-1;pass++)
    {
        cout<<"Pass:"<<pass+1<<endl;
        for(int i=0;i<e;i++)
        {   Edge curr=input[i];
           
                if(weight[curr.source]!=INT_MAX and weight[curr.dest]>weight[curr.source]+curr.weight)
                {
                    weight[curr.dest]=weight[curr.source]+curr.weight;
                }
        
        }
            for(int i=0;i<n;i++)
        {
            cout<<weight[i]<<"  ";
        }
        cout<<endl;
        
    }
     for(int i=0;i<e;i++)
        {   Edge curr=input[i];
           
                if(weight[curr.source]!=INT_MAX and weight[curr.dest]>weight[curr.source]+curr.weight)
                {
                    cout<<"Graph contain Negetive cycle!";
                    return;
                }
        
        }
}
int main()
{
    int n,e;
    cin>>n>>e;
    Edge* input = new Edge[e];
    for(int i=0;i<e;i++)
        {
            int s,d,w;
            cin>>s>>d>>w;
            input[i].source = s;
            input[i].dest = d;
            input[i].weight = w;
        }
    bellman_ford(input,n,e,0);

    return 0;
}