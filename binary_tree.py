class Node:
    def __init__(self, symptom, medication=None, description=None):
        self.symptom = symptom  # Sintoma representado pelo nó
        self.medication = medication  # Medicação recomendada para o sintoma
        self.description = description  # Descrição do sintoma
        self.left = None  # Filho à esquerda na árvore binária
        self.right = None  # Filho à direita na árvore binária

class BinaryTree:
    def __init__(self):
        self.root = None  # Raiz da árvore binária

    def is_empty(self):
        return self.root is None  # Verifica se a árvore está vazia

    def add(self, symptom, medication=None, description=None):
        new_node = Node(symptom, medication, description)  # Cria um novo nó
        if self.is_empty():
            self.root = new_node  # Define o nó como raiz se a árvore estiver vazia
        else:
            self._insert(self.root, new_node)  # Insere o nó na posição correta

    def _insert(self, root, new_node):
        if new_node.symptom < root.symptom:
            if root.left is None:
                root.left = new_node  # Insere à esquerda se não houver filho esquerdo
            else:
                self._insert(root.left, new_node)  # Continua a inserção recursivamente à esquerda
        elif new_node.symptom > root.symptom:
            if root.right is None:
                root.right = new_node  # Insere à direita se não houver filho direito
            else:
                self._insert(root.right, new_node)  # Continua a inserção recursivamente à direita

    def search(self, symptom):
        return self._search(self.root, symptom)  # Inicia a busca a partir da raiz

    def _search(self, root, symptom):
        if root is None:
            return None  # Retorna None se o nó não for encontrado
        if symptom == root.symptom:
            return root  # Retorna o nó se o sintoma corresponder
        elif symptom < root.symptom:
            return self._search(root.left, symptom)  # Busca recursivamente à esquerda
        else:
            return self._search(root.right, symptom)  # Busca recursivamente à direita

    def get_medication_recommendation(self, symptoms):
        recommended_medications = set()  # Conjunto para armazenar medicamentos recomendados
        for symptom in symptoms:
            node = self.search(symptom)
            if node and node.medication:
                recommended_medications.add(node.medication)  # Adiciona a medicação ao conjunto
        return recommended_medications

    def ask_symptoms(self):
        symptoms = []
        while True:
            symptom = input("Digite um sintoma que você está sentindo (ou 'não' para terminar): ").strip().lower()
            if symptom == 'não':
                break  # Encerra a entrada de sintomas
            node = self.search(symptom)
            if node:
                print(f"Sintoma: {node.symptom}\nDescrição: {node.description}")  # Exibe a descrição do sintoma
                symptoms.append(symptom)  # Adiciona o sintoma à lista de sintomas
            else:
                print(f"Sintoma '{symptom}' não encontrado.")  # Mensagem de erro se o sintoma não for encontrado
        return symptoms