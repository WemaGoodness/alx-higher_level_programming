#include "lists.h"

/**
 * check_cycle - checks if singly linked list has a cycle
 * @list: pointer to beginning of node
 *
 * Return: 0 if no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
