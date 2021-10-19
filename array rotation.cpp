#include <stdio.h>
void rotatebyone(int a[],int n);

void rotate(int a[],int d,int n)
{
     int i;
     for(i=0;i<d;i++)
     rotatebyone(a,n);
}     
void rotatebyone(int a[],int n)
{
     int temp=a[0],i;
     for(i=0;i<n-1;i++)
     a[i]=a[i+1];
     a[i]=temp;
}     
void printarray(int a[],int n)
{
     int i;
     for(i=0;i<n;i++)
     printf("%d",a[i]);
}     
int main() 
{
int a[]={1,2,3,4,5,6,7};
rotate(a,2,7);
printarray(a,7);

	return 0;
}