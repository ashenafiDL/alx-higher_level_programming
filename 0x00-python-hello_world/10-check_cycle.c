#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a linked lists
 *
 * @list: pointer to the first node
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1, *temp2;

	temp1 = list;
	while (temp1 != NULL)
	{
		temp2 = temp1->next;
		while (temp2 != NULL)
		{
			if (temp2->next == temp1)
				return (1);

			temp2 = temp2->next;
		}
		temp1 = temp1->next;
	}

	return (0);
}
