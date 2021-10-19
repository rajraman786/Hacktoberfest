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
struct node *insert_bef(struct node *);
struct node *insert_aft(struct node *);
struct node *delete_beg(struct node *);
struct node *delete_end(struct node *);
struct node *delete_node(struct node *);
struct node *delete_aft(struct node *);
struct node *delete_list(struct node *);
struct node *sort(struct node *);
struct node *reverse_list(struct node *);
int main()
{
    int option;
    printf("****MENU LIST****\n");
    printf("1:create list\n");
    printf("2:display list\n");
    printf("3:insert at begning\n");
    printf("4:insert at last\n");
    printf("5:insert before given node\n");
    printf("6:insert after given node\n");
    printf("7:delete at begning\n");
    printf("8:delete at last\n");
    printf("9:delete after given node\n");
    printf("10:delete  node\n");
    printf("11:delete list\n");
    printf("12:sort list\n");
    printf("13:to reverse list\n");
    printf("14:to exit list\n");
    scanf("%d",&option);
    while(option!=14)
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
            case 5:start=insert_bef(start);
                   break;
            case 6:start=insert_aft(start);
                   break;
            case 7:start=delete_beg(start);
                   break;
            case 8:start=delete_end(start);
                   break;
            case 9:start=delete_aft(start);
                   break;
            case 10:start=delete_node(start);
                   break;
            case 11:start=delete_list(start);
                   break;
            case 12:start=sort(start);
                    break;
            case 13:start=reverse_list(start);
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
            new_node->next=NULL;
        }
        else
        {
            ptr=start;
            while(ptr->next!=NULL)
                ptr=ptr->next;
            ptr->next=new_node;
            new_node->next=NULL;
        }
        scanf("%d",&num);
    }
    return start;
}
struct node *display(struct node *start)
{
    int k=0;
    struct node *ptr;
    ptr=start;
    while(ptr!=NULL)
        {printf("->%d\n",ptr->data);
        ptr=ptr->next;
        k++;}
    if(k==0)
        printf("list is empty.");
    return start;
}
struct node *insert_beg(struct node *start)
{
    int num;
    scanf("%d",&num);
    struct node *new_node;
    new_node= (struct node*)malloc(sizeof(struct node));
    new_node->data=num;
    new_node->next=start;
    start=new_node;
    return start;
}
struct node *insert_end(struct node *start)
{
    int num;
    scanf("%d",&num);
    struct node *ptr,*new_node;
    new_node= (struct node*)malloc(sizeof(struct node));
    new_node->data=num;
    new_node->next=NULL;
    ptr=start;
    if(start==NULL){
        start=new_node;
    }else{
    while(ptr->next!=NULL)
    ptr=ptr->next;
    ptr->next=new_node;}
    return start;
}
struct node *insert_bef(struct node *start)
{
    if(start==NULL){printf("empty list.\n");}
    else{int num,val;
    printf("enter number than given node value\n");
    scanf("%d%d",&num,&val);
    struct node *preptr,*ptr,*new_node;
    new_node= (struct node*)malloc(sizeof(struct node));
    new_node->data=num;
    ptr=start;
    if(start->next==NULL){new_node->next=start;start=new_node;}
    else{preptr=ptr;
    while(ptr->data!=val)
    {preptr=ptr;
    ptr=ptr->next;}
    preptr->next=new_node;
    new_node->next=ptr;}}
    return start;
}
struct node *insert_aft(struct node *start)
{
    if(start==NULL){printf("empty list.\n");}
    else{int num,val;
    printf("enter number than given node value\n");
    scanf("%d%d",&num,&val);
    struct node *ptr,*new_node;
    new_node= (struct node*)malloc(sizeof(struct node));
    new_node->data=num;
    ptr=start;
    while(ptr->data!=val)
    ptr=ptr->next;
    new_node->next=ptr->next;
    ptr->next=new_node;}
    return start;
}
struct node *delete_beg(struct node *start)
{
    struct node *ptr;
    ptr=start;
    if(start==NULL){printf("list is empty.\n");}
    else{start=start->next;
    free(ptr);}
    return start;
}
struct node *delete_end(struct node *start)
{
    struct node *ptr,*preptr;
    ptr=start;
    if(start==NULL){printf("list is empty.\n");}
    else if(start->next==NULL){start==NULL;free(ptr);}
    else{while(ptr->next!=NULL)
    {preptr=ptr;
    ptr=ptr->next;}
    preptr->next=NULL;
    free(ptr);}
    return start;
}
struct node *delete_aft(struct node *start)
{
    if(start==NULL || start->next==NULL){printf("there is no sufficient element\n");}
    else{printf("enter the node value\n");
    int num;
    scanf("%d",&num);
    struct node *ptr,*nextptr;
    ptr=start;
    if(start->data==num){start=start->next;}
    else{while(ptr->data!=num)
    {ptr=ptr->next;
    nextptr=ptr->next;}
    ptr->next=nextptr->next;}
    free(nextptr);}
    return start;
}
struct node *delete_node(struct node *start)
{
    if(start==NULL){printf("list is empty\n");}
    else{printf("enter the node value\n");
    int num;
    scanf("%d",&num);
    struct node *ptr,*preptr;
    ptr=start;
    if(start->data==num){start=start->next;}
    else{while(ptr->data!=num)
    {preptr=ptr;
    ptr=ptr->next;}
    preptr->next=ptr->next;}
    free(ptr);}
    return start;
}
struct node *delete_list(struct node *start)
{
    struct node *ptr;
    if(start!=NULL){
        ptr=start;
        while(ptr!=NULL){
            start=delete_beg(start);
            ptr=start;
        }
    }
    return start;
}
struct node *sort(struct node *start)
{
    int temp;
    struct node *ptr1,*ptr2;
    ptr1=start;
    while(ptr1->next!=NULL){
        ptr2=ptr1->next;
        while(ptr2!=NULL){
            if(ptr2->data<ptr1->data)
            {
                temp=ptr1->data;
                ptr1->data=ptr2->data;
                ptr2->data=temp;
            }
            ptr2=ptr2->next;
        }
        ptr1=ptr1->next;
    }
    return start;
}
struct node *reverse_list(struct node *start)
{
    if(start==NULL){printf("list is empty\n");}
    else{struct node *ptr, *preptr, *temp;
    preptr=NULL;
    ptr=start;
    while(ptr->next!=NULL)
    {
        temp=ptr->next;
        ptr->next=preptr;
        preptr=ptr;
        ptr=temp;
    }
    start=ptr;
    start->next=preptr;
    }
    return start;
}
