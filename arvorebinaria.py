class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_em_nivel_recursivo(self.raiz, valor)

    def _inserir_em_nivel_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_em_nivel_recursivo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_em_nivel_recursivo(no.direita, valor)
    
    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_pre_ordem_recursivo(self.raiz)

    def mostrar_pre_ordem_recursivo(self, no):
        print(no.valor, end=" ")
        if no.esquerda is not None:
            self.mostrar_pre_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pre_ordem_recursivo(no.direita)
    
    def mostrar_in_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_in_ordem_recursivo(self.raiz)

    def mostrar_in_ordem_recursivo(self, no):
        if no.esquerda is not None:
            self.mostrar_in_ordem_recursivo(no.esquerda)
        print(no.valor, end=" ")
        if no.direita is not None:
            self.mostrar_in_ordem_recursivo(no.direita)
    
    def mostrar_pos_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_pos_ordem_recursivo(self.raiz)

    def mostrar_pos_ordem_recursivo(self, no):
        if no.esquerda is not None:
            self.mostrar_pos_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pos_ordem_recursivo(no.direita)
        print(no.valor, end=" ")

    def mostrar_ordem_niveis(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            fila = [self.raiz]
            while fila:
                no = fila.pop(0)
                print(no.valor, end=" ")
                if no.esquerda is not None:
                    fila.append(no.esquerda)
                if no.direita is not None:
                    fila.append(no.direita)

#Exemplo de uso
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

print("Pre-ordem:")
arvore.mostrar_pre_ordem()

print("\nIn-ordem:")
arvore.mostrar_in_ordem()

print("\nPós-ordem:")
arvore.mostrar_pos_ordem()

print("\nOrdem de Níveis:")
arvore.mostrar_ordem_niveis()