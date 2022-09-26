#include "lists.h"

/**
 * is_palindrome - checks if a linked list is plindrome or not
 * @head: address of the head pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *second_half_ptr;

	if (*head == NULL)
		return (1);
	else
	{
		second_half_ptr = get_middle(head);
		reverse(&second_half_ptr);
	}

	return (compare(head, &second_half_ptr));
}

/**
 * get_middle - gets the middle node of a singly linked list
 * @head: address of pointer to the first node
 *
 * Return: the middle node
 */
listint_t *get_middle(listint_t **head)
{
	listint_t *middle, *last;

	middle = *head;
	last = *head;

	while (last != NULL)
	{
		middle = middle->next;
		last = last->next->next;
	}

	return (middle);
}

/**
 * reverse - reverses a liked list
 * @head: pointer to the fifrst node
 */
void reverse(listint_t **head)
{
	listint_t *prev, *curr, *nxt;

	prev = NULL;
	curr = *head;
	nxt = NULL;

	while (curr != NULL)
	{
		nxt = curr->next;
		curr->next = prev;
		prev = curr;
		curr = nxt;
	}

	*head = prev;
}

/**
 * compare - compares two linked lists
 * @first: the first list
 * @second: the second list
 *
 * Return: 1 if the are equal, 0 otherwise
 */
int compare(listint_t **first, listint_t **second)
{
	listint_t *f = *first;
	listint_t *s = *second;

	while (f != NULL && s != NULL)
	{
		if (f->n != s->n)
			return (0);
		f = f->next;
		s = s->next;
	}

	return (1);
}
