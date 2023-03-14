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
    int count = 0;
    int i;
    listint_t *curr = *head;
    int arr[100]; 
    while (curr != NULL)
    {
        arr[count++] = curr->n;
        curr = curr->next;
    }

    for (i = 0; i < count / 2; i++)
    {
        if (arr[i] != arr[count - 1 - i])
        {
            return (0);
        }
    }

    return (1);
}
