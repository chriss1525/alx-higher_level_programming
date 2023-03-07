#include "lists.h"
/**
 *check_cycle - checks if a singly linked list has a cycle in it
 * @list: first item in linked list
 * Return: 0(success) 1(fail)
 */
int check_cycle(listint_t *list)
{
	listint_t *new = list;
	listint_t *temp = list;

	if (!list)
		return (0);

	while (new &&temp && temp->next)
	{
		new = new->next;
		temp = temp->next->next;

		if (new == temp)
			return (1);
	}

	return (0);
}
