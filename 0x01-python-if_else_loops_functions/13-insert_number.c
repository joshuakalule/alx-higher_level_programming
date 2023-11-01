#include "lists.h"

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: pointer to a pointer to the list
 * @number: data to add
 *
 * Return: address of the new node | NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *node, *parent;

	new = malloc(sizeof(listint_t));
	if (!head || !new)
		return (NULL);
	new->n = number;
	node = *head;
	parent = NULL;
	while (node)
	{
		if (node->n > number)
			break;
		parent = node;
		node = node->next;
	}
	new->next = node;
	if (parent)
		parent->next = new;
	else
		*head = new;
	return (new);
}
