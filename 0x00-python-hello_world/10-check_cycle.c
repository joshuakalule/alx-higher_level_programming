#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: 0 (no cycle) | 1 (cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *hare, *snail;

	if (!list)
		return (0);
	snail = list;
	if (list->next)
		hare = list->next->next;
	else
		hare = list->next;
	while (hare)
	{
		if (hare == snail)
			return (1);
		if (hare->next)
			hare = hare->next->next;
		else
			hare = hare->next;
		snail = snail->next;
	}
	return (0);
}
