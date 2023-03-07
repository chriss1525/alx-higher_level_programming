#include "lists.h"
/**
 *check_cycle - checks if a singly linked list has a cycle in it
 * @list: first item in linked list
 * Return: 0(success) 1(fail)
 */
int check_cycle(listint_t *list)
{
	listint_t *new, *temp;
	int i, j;

	temp = list;
	i = 0;

	while(temp)
	{
		if (i != 0)
		{
			new = list;
			j = 0;
			while (j < i)
			{
				if (new == temp)
					return (1);
				j++;
				new = new->next;
			}
		}
		temp = temp->next;
		i++;
	}

	return (0);
}
