#include <stdio.h>

struct List
{ 
 int data;
 struct List *next;
};


int Search (struct List *node, int X)
{ 
    while (node) 
    { 
        if (node->data == X)	return 1;       
            node = node->next;  
    } 
    return 0;
}


struct List *recreverse(struct List *head)
{  
    if(head && head->next) 
    {
        struct List *temp = head, *t;
        if(head->next)	
        {	
            head = recreverse(head->next);
            t = head;
            while (t->next)	    
            t = t->next;
            t->next = temp;
            temp->next = NULL;	
        }    
    }  
    return head;
}



void reverse(struct List **head)
{ 
    struct List *p = NULL, *c = *head, *n;  
    while (c)    
    {  
        n = c->next;
        c->next = p;
        p = c;
        c = n;
    }
    *head = p;
}


int Cycle(struct List *node)
{
    struct List *t1,*t2;t1=t2=node;
        while (t2)    
        {
            t2=t2->next; 
            if (t2==t1)	
                return 1;
            t1 = t1->next; 
            if(t2) t2=t2->next; 
        }  
    return 0;
}

struct List *addatbeg(struct List *head, int i)
{
    struct List *temp = (struct List *) malloc (sizeof (struct List));  
    temp->data = i; 
    temp->next = head; 
    return temp;
}


void Deleteatbeg (struct List **node)
{  
    struct List *temp = *node; 
    if (*node)
    {
        *node = (*node)->next;
        free (temp);
    }
 }



void Addatbeg(struct List **head, int i)
{ 
    struct List *temp = (struct List *) malloc (sizeof (struct List));  
    temp->data = i; 
    temp->next = *head;
    *head = temp;
}
