#include <stdio.h>
#include <malloc.h>
struct node
{
    struct node *prev;
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
struct node *delete_node(struct node *);
struct node *delete_list(struct node *);
struct node *reverse_list(struct node *);
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
    printf("7:delete  given node\n");
    printf("8:delete list\n");
    printf("9:reverse list\n");
    printf("10: to exit\n");
    scanf("%d",&option);
    while(option!=10)
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
            case 7:start=delete_node(start);
                   break;
            case 8:start=delete_list(start);
                   break;
            case 9:start=reverse_list(start);
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
            new_node->prev=start;
        }
        else
        {
            ptr=start;
            while(ptr->next!=start)
                ptr=ptr->next;
            ptr->next=new_node;
            new_node->next=start;
            new_node->prev=ptr;
            start->prev=new_node;
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
        new_node->prev=start;
    }
    else
    {ptr=start;
    while(ptr->next!=start){
        ptr=ptr->next;
    }
    ptr->next=new_node;
    new_node->prev=ptr;
    new_node->next=start;
    start->prev=new_node;
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
        new_node->next=start;
        new_node->prev=start;
    }
    else{ptr=start;
    while(ptr->next!=start){
        ptr=ptr->next;
    }
    ptr->next=new_node;
    new_node->prev=ptr;
    new_node->next=start;
    start->prev=new_node;}
    return start;
}
struct node *delete_beg(struct node *start)
{
    if(start==NULL){printf("empty list\n");}
    else{struct node *ptr;
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
    start=ptr->next;
    start->prev=ptr;}}
    return start;
}
struct node *delete_end(struct node *start)
{
    if(start==NULL){printf("empty list.\n");}
    else{struct node *ptr,*preptr;
    ptr=start;
    if(start->next==start){start=NULL;}
    else{while(ptr->next!=start){
        preptr=ptr;
        ptr=ptr->next;
    }
    preptr->next=start;
    start->prev=preptr;}
    free(ptr);}
    return start;
}
struct node *delete_node(struct node *start)
{
    if(start==NULL){printf("empty list\n");}
    else{struct node *ptr;
    int num;
    printf("enter the node value");
    scanf("%d",&num);
    ptr=start;
    if(start->next==start){start=NULL;}
    else{while(ptr->data!=num)
        ptr=ptr->next;
    ptr->prev->next=ptr->next;
    ptr->next->prev=ptr->prev;
    if(ptr==start)
        start=start->next;}
    free(ptr);}
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
struct node *reverse_list(struct node *start)
{
    if(start!=NULL){struct node *ptr, *temp;
    ptr=start;
    while(ptr->next!=start)
    {
        temp=ptr->next;
        ptr->next=ptr->prev;
        ptr->prev=temp;
        ptr=ptr->prev;
    }
    temp=ptr->next;
    ptr->next=ptr->prev;
    ptr->prev=temp;
    start=ptr;}
    else{printf("empty list\n");}
    return start;
}


