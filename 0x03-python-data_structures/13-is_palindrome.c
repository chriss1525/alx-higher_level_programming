#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: pointer to pointer to head node
 *
 * Return: 0 if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
    int *list, len, i;
    listint_t *current;

    list = malloc(sizeof(int));
    if (list == NULL)
        exit(EXIT_FAILURE);

    current = *head;
    len = 1;

    /* traverse the linked list */
    while (current)
    {
        list[len++ - 1] = current->n;
        list = realloc(list, sizeof(int) * len);
        current = current->next;
    }

    len -= 1;
    i = 0;

    /* check for palindrome */
    while (i <= len / 2)
    {
        if (list[i] != list[len - i - 1])
            return (0);

        i++;
    }

    return (1);
}
