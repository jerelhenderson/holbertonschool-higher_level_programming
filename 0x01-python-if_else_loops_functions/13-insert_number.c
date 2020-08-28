#include "lists.h"


/**
 * insert_number - function inserts number into sorted singly linked list
 *
 * @list: list to check
 * Return: address of new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	current = *head;

	if (*head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	current = current->next;

	while (current->next != NULL)
	{
		if (new_node->n > current->n && new_node->n < current->next->n)
		{
                        new_node->next = current->next;
                        current->next = new_node;
			break;
		}
		current = current->next;
	}
	return (0);
}
