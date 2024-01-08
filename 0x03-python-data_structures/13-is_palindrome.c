#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: start of list
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *temp = *head;
    int array[2048];
    int i = 0;
    int j;

    if (head == NULL || *head == NULL)
        return (1);

    while (temp != NULL)
    {
        array[i] = temp->n;
        temp = temp->next;
        i++;
    }

    for (j = 0; j < (i / 2); j++)
    {
        if (array[j] != array[i - 1 - j])
            return (0);
    }
    return (1);
}
