class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Checar se a lista não está vazia. Se estiver, podemos retornar a head pq não terá nada para ordenar
        if not head:
            return head

        node = head
        sorted_list = []

        # Atravessar a lista encadeada e extrair os valores para o vetor
        while node:
            sorted_list.append(node.val)
            node = node.next

        # Ordenar o vetor
        sorted_list.sort()

        # Atravessar a lista encadeada dnv para atualizar os vetores
        node = head
        for val in sorted_list:
            node.val = val
            node = node.next

        return head