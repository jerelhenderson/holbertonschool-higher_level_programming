#include "lists.h"


/**
 * check_cycle - check for loop in linked list
 *
 * @list: list to check
 * Return: 0 if no cycle, 1 if a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *func_head;
	listint_t *func_trav;

	func_head = list;
	func_trav = list;

	if (list == NULL)
		return (0);

	while (func_head->next != NULL)
	{
		func_trav = func_headcd->next;
		while (func_trav->next != NULL)
		{
			if (func_head->next == func_trav->next)
				return (1);
			func_trav = func_trav->next;
		}
		func_head = func_head->next;
	}
	return (0);
}
