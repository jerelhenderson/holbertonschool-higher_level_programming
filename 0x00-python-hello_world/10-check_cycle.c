#include "lists.h"

/**
 * check_cycle - check for loop in linked list
 *
 * @list: list to check
 * Return: 0 if no cycle, 1 if a cycle
 */
int check_cycle(listint_t *list)
{
  listint_t *tmp1;
  listint_t *tmp2;

  tmp1 = list;
  tmp2 = list->next;

  if (list == NULL)
    return (0);

  while (tmp2 != NULL)
    {
      tmp2 = tmp2->next->next;
      tmp1 = tmp1->next;
      if (tmp1 == tmp2)
	return (1);
    }
  return (0);
}
