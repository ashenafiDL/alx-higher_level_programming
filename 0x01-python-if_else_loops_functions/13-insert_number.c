#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: address of the head pointer
 * @number: the number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *temp, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	else
	{
		temp = *head;
		prev = *head;
		while (temp->n <= number)
		{
			if (temp->next == NULL)
			{
				prev = temp;
				break;
			}
			prev = temp;
			temp = temp->next;
		}
		if (*head == temp)
		{
			new->next = *head;
			*head = new;
		}
		else
		{
			new->next = prev->next;
			prev->next = new;
		}
		return (new);
	}
	return (NULL);
}
