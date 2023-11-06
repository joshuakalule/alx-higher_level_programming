#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse - reverses the list
 * @start: node to start reversing
 */
void reverse_at(listint_t **start)
{
    listint_t *node1, *node2;
    
    node1 = (*start)->next;
    while (node1)
    {
        node2 = node1->next;
        node1->next = *start;
        *start = node1;
        node1 = node2;
    }
}

/**
 * revert_at - reverts changes made on a list
 * @start: node to start reverting
 * @end: node to end at
 */
void revert_at(listint_t *end, listint_t *start)
{
    listint_t *node1, *node2;

    node1 = end->next;
    end->next = NULL;
    node2 = end;
    end = node1;
    while (start != end)
    {
        node1 = end->next;
        end->next = node2;
        node2 = end;
        end = node1;
    }
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a pointer to the head of the list
 * Return: 0 (False) | 1 (True)
 */
int is_palindrome(listint_t **head)
{
    listint_t *hare, *snail;
    listint_t *node, *end;

    if (!head || !*head)
        return (1);
    snail = *head;
    if ((*head)->next)
        hare = (*head)->next->next;
    else
        return (1);
    while (hare)
    {
        snail = snail->next;
        hare = hare->next;
        if (hare)
            hare = hare->next;
    }
    hare = snail;
    /*printf(" mid: %d\n", hare->n);*/
    reverse_at(&snail);
    end = snail;
    node = *head;
    while (snail != hare)
    {
        /*printf(" %d - %d \n", node->n, snail->n);*/
        if (snail->n != node->n)
        {
            revert_at(end, hare);
            return (0);
        }
        snail = snail->next;
        node = node->next;
    }
    revert_at(end, hare);
    return (1);
}
