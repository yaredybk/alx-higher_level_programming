#ifndef LIST_H
#define LIST_H

#include <stdlib.h>

/**
 * struct listptr_s - a sigly linked list of pointers
 * @ptr: current value
 * @next: next pointer
 *
 * Description: singly listed list of pointers
 */
typedef struct listptr_s
{
	int* ptr;
	struct listptr_s *next;
} listptr_t;


/**
 * struct listint_s - a sigly linked list
 * @val: current value
 * @next: next pointer
 *
 * Description: singly listed list
 */
typedef struct listint_s
{
	int val;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);

#endif /* LIST_H */
