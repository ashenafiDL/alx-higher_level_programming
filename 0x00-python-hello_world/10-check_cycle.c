#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a linked lists
 *
 * @list: pointer to the first node
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;
	while (fast && slow && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
