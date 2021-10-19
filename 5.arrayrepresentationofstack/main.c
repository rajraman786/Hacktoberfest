#include <stdio.h>
#define MAX 3
int st[MAX],top=-1;
void push(int *st,int val);
int pop(int *st);
int peek(int *st);
void display( int *st);
int main()
{
    int option,n,val;
    printf("enter 1:to add top element\n");
    printf("enter 2:to delete top element\n");
    printf("enter 3:to display top element\n");
    printf("enter 4:to display stack element\n");
    printf("enter 5:to exit\n");
    scanf("%d",&option);
    while(option!=5)
    {
        switch(option)
        {
            case 1:printf("enter the number\n");
                   scanf("%d",&n);
                   push(st,n);
                   break;
            case 2:val=pop(st);
                   if(val!=-1)
                    printf("%d is deleted\n",val);
                   break;
            case 3:val=peek(st);
                   if(val!=-1)
                   printf("the top value is %d\n",val);
                   break;
            case 4:display(st);
                    break;
        }
        scanf("%d",&option);
    }
    return 0;
}
void push(int *st, int n)
{
    if(top==MAX-1)
        printf("overflow\n");
    else
    {
        top=top+1;
        st[top]=n;
    }
}
int pop(int *st)
{
    int val;
    if(top==-1){
        printf("underflow\n");
        return -1;
    }
    else{
        val=st[top];
        top--;
        return val;
    }
}
int peek(int *st)
{
    int val;
    if(top==-1){
        printf("stack is empty\n");
        return -1;
    }
    else{
        val=st[top];
        return val;
    }
}
void display(int *st)
{
    if(top==-1)
        printf("stack is empty\n");
    else{
        for(int i=0;i<=top;i++)
            printf("%d\n",st[i]);
    }
}
