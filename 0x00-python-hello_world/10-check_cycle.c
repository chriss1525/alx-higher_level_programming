#include "lists.h"
/**
 *check_cycle - checks if a singly linked list has a cycle in it
 * @list: first item in linked list
 * Return: 0(success) 1(fail)
 */
int check_cycle(listint_t *list)
{
	listint_t *new;

	new = list->next;
	while (new->next)
	{
		if (new->next == list)
			return (0);
		if (new->next == new)
			return (0);
		new = new->next;
	}
	return (1);
}
