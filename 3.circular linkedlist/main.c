#include <stdio.h>
#include <malloc.h>
struct node
{
    int data;
    struct node *next;
};
struct node *start=NULL;
struct node *create(struct node *);
struct node *display(struct node *);
struct node *insert_beg(struct node *);
struct node *insert_end(struct node *);
struct node *delete_beg(struct node *);
struct node *delete_end(struct node *);
struct node *delete_aft(struct node *);
struct node *delete_list(struct node *);
int main()
{
    int option;
    printf("****MENU LIST****\n");
    printf("1:create list\n");
    printf("2:display list\n");
    printf("3:insert at begning\n");
    printf("4:insert at last\n");
    printf("5:delete at begning\n");
    printf("6:delete at last\n");
    printf("7:delete after given node\n");
    printf("8:delete list\n");
    printf("9: to exit\n");
    scanf("%d",&option);
    while(option!=9)
    {
        switch(option)
        {
            case 1:start=create(start);
                   break;
            case 2:start=display(start);
                   break;
            case 3:start=insert_beg(start);
                   break;
            case 4:start=insert_end(start);
                   break;
            case 5:start=delete_beg(start);
                   break;
            case 6:start=delete_end(start);
                   break;
            case 7:start=delete_aft(start);
                   break;
            case 8:start=delete_list(start);
                   break;
        }
        scanf("%d",&option);
    }
    return 0;
}
struct node *create(struct node *start)
{
    struct node *new_node,*ptr;
    int num;
    ptr=start;
    printf("-1 to stop create the list\n");
    scanf("%d",&num);
    while(num!=-1)
    {
        new_node= (struct node*)malloc(sizeof(struct node));
        new_node->data=num;
        if(start==NULL)
        {
            start=new_node;
            new_node->next=start;
        }
        else
        {
            ptr=start;
            while(ptr->next!=start)
                ptr=ptr->next;
            ptr->next=new_node;
            new_node->next=start;
        }
        scanf("%d",&num);
    }
    return start;
}
struct node *display(struct node *start)
{
    struct node *ptr;
    ptr=start;
    if(start==NULL)
        printf(" empty list ");
    else
    {while(ptr->next!=start)
    {printf("->%d\n",ptr->data);
    ptr=ptr->next;}
    printf("->%d\n",ptr->data);}
    return start;
}
struct node *insert_beg(struct node *start)
{
    struct node *new_node ,*ptr;
    int num;
    scanf("%d",&num);
    new_node= (struct node*)malloc(sizeof(struct node));
    new_node->data=num;
    if(start==NULL)
    {
        start=new_node;
        new_node->next=start;
    }
    else
    {ptr=start;
    while(ptr->next!=start){
        ptr=ptr->next;
    }
    ptr->next=new_node;
    new_node->next=start;
    start=new_node;}
    return start;
}
struct node *insert_end(struct node *start)
{
    struct node *new_node ,*ptr;
    int num;
    scanf("%d",&num);
    new_node= (struct node*)malloc(sizeof(struct node));
    new_node->data=num;
    if(start==NULL){
        start=new_node;
        new_node=start;
    }
    else{ptr=start;
    while(ptr->next!=start){
        ptr=ptr->next;
    }
    ptr->next=new_node;
    new_node->next=start;}
    return start;
}
struct node *delete_beg(struct node *start)
{
    struct node *ptr;
    ptr=start;
    while(ptr->next!=start){
        ptr=ptr->next;
    }
    if(ptr==start){
        start=NULL;
    }
    else
    {ptr->next=start->next;
    free(start);
    start=ptr->next;}
    return start;
}
struct node *delete_end(struct node *start)
{
    struct node *ptr,*preptr;
    ptr=start;
    while(ptr->next!=start){
        preptr=ptr;
        ptr=ptr->next;
    }
    preptr->next=start;
    free(ptr);
    return start;
}
struct node *delete_aft(struct node *start)
{
    struct node *ptr,*nextptr;
    int num;
    printf("enter the node value");
    scanf("%d",&num);
    ptr=start;
    while(ptr->data!=num){
        ptr=ptr->next;
        nextptr=ptr->next;
    }
    ptr->next=nextptr->next;
    if(nextptr==start)
        start=ptr->next;
    free(nextptr);
    return start;
}
struct node *delete_list(struct node *start)
{
    while(start->next!=start){
            start=delete_beg(start);
            }
    start=delete_beg(start);
    return start;
}


