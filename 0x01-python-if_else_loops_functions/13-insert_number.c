#include "lists.h"

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: beginning of list
 * @number: number to insert
 *
 * Return: Always a success
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(listint_t));

    if (new_node == NULL)
        return (NULL);

    new_node->n = number;

    if (*head == NULL || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
    }
    else
    {
        listint_t *current = *head;
        while (current->next != NULL && current->next->n < number)
            current = current->next;

        new_node->next = current->next;
        current->next = new_node;
    }

    return (new_node);
}

