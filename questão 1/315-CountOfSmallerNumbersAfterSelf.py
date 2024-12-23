class Solution:
    def countSmaller(self, nums):
        """
        Dado um array nums, conta quantos números menores estão à direita de cada elemento.
        Retorna uma lista com esses valores.
        """

        def ordenar(indices):
            """
            Função recursiva que ordena os índices com base nos valores em nums e, ao mesmo tempo,
            calcula quantos números menores estão à direita de cada elemento.

            Args:
                indices (List[int]): Lista de índices representando elementos em nums.

            Returns:
                List[int]: Lista de índices ordenados.
            """
            # Divide os índices pela metade para usar a abordagem "Dividir e Conquistar"
            metade = len(indices) // 2  
            if metade:  # Só divide se houver elementos suficientes
                # Divide os índices em duas partes e ordena recursivamente
                esquerda = ordenar(indices[:metade])  # Parte esquerda
                direita = ordenar(indices[metade:])  # Parte direita

                # Combina os resultados das duas partes
                for i in range(len(indices) - 1, -1, -1):  # Percorre os índices de trás para frente
                    # Se a direita estiver vazia ou o maior valor da esquerda for maior que o maior da direita
                    if not direita or (esquerda and nums[esquerda[-1]] > nums[direita[-1]]):
                        # O elemento da esquerda domina, e todos os da direita ainda são menores
                        contagem_menores[esquerda[-1]] += len(direita)
                        indices[i] = esquerda.pop()  # Coloca o índice na posição correta
                    else:
                        # O elemento da direita é menor ou igual
                        indices[i] = direita.pop()  # Coloca o índice na posição correta

            return indices  # Retorna os índices ordenados

        # Inicializa a lista para contar números menores à direita para cada elemento
        contagem_menores = [0] * len(nums)

        # Inicializa a ordenação e cálculo com os índices dos elementos em nums
        ordenar(list(range(len(nums))))

        return contagem_menores
