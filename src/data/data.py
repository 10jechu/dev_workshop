class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        left = 0
        right = len(lista) - 1
        while left < right:
            lista[left], lista[right] = lista[right], lista[left]
            left += 1
            right -= 1
        return lista
    
    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        vistos = []
        vistos_con_tipo = []
        for elemento in lista:
            tipo_elemento = type(elemento)
            if (elemento, tipo_elemento) not in vistos_con_tipo:
                vistos.append(elemento)
                vistos_con_tipo.append((elemento, tipo_elemento))
        return vistos
    
    def merge_ordenado(self, lista1, lista2):
        resultado = []
        i = 0
        j = 0
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1
        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1
        return resultado
    
    def rotar_lista(self, lista, k):
        if not lista or k == 0:
            return lista
        k = k % len(lista)
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_esperada = (n * (n + 1)) // 2
        suma_actual = sum(lista)
        return suma_esperada - suma_actual
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        pila = []
        
        def push(elemento):
            pila.append(elemento)
        
        def pop():
            if not pila:
                return None
            return pila.pop()
        
        def peek():
            if not pila:
                return None
            return pila[-1]
        
        def is_empty():
            return len(pila) == 0
        
        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }
    
    def implementar_cola(self):
        cola = []
        
        def enqueue(elemento):
            cola.append(elemento)
        
        def dequeue():
            if not cola:
                return None
            return cola.pop(0)
        
        def peek():
            if not cola:
                return None
            return cola[0]
        
        def is_empty():
            return len(cola) == 0
        
        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }
    
    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []
        filas = len(matriz)
        columnas = len(matriz[0])
        transpuesta = [[0] * filas for _ in range(columnas)]
        
        for i in range(filas):
            for j in range(columnas):
                transpuesta[j][i] = matriz[i][j]  
        
        return transpuesta