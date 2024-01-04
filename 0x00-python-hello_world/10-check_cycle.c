#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: input list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *list1;
	listptr_t *list2;
	listptr_t *first;
	
	if(list1 == NULL || list1->next == NULL)
		return (0);

	list1 = list;
	list2->ptr = list1->val;
	list2->next = (int*) malloc(sizeof(listptr_t));
	first = list2;

	while (list1->next != NULL)
	{
	}
}
