#include <stdio.h>

struct List
{ 
 int data;
 struct List *next;
};

void Addatbeg(struct List **head, int i)
{ 
    struct List *temp = (struct List *) malloc (sizeof (struct List));  
    temp->data = i; 
    temp->next = *head;
    *head = temp;
}

struct List *addatbeg(struct List *head, int i)
{
    struct List *new_head = (struct List *) malloc (sizeof (struct List));  
    new_head->data = i; 
    new_head->next = head; 
    return new_head;
}

int main()
{
    struct List *head = (struct List*)malloc(sizeof(struct List));

    int size_of_list,pos;
    scanf("%d",&size_of_list);
    int *array = malloc(sizeof(int)*size_of_list);
    for (int i = 0; i < size_of_list; i++)
    {
        scanf("%d",&array[i]);
    }


    head->data = array[0];
    
    for (int i = 1; i < size_of_list; i++)
    {
        
    }
    

}