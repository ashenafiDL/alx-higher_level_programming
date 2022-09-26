#include "lists.h"

/**
 * is_palindrome - checks if a linked list is plindrome or not
 * @head: address of the head pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half;
	listint_t *slow_prev= *head;

	if (*head == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow_prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
		slow = slow->next;

	second_half = slow;
	slow_prev->next = NULL;
	reverse(&second_half);
	return (compare(head, &second_half));
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

	while (s != NULL)
	{
		if (f->n != s->n)
			return (0);
		f = f->next;
		s = s->next;
	}

	return (1);
}
