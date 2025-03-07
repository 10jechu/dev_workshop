class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triángulo de Pascal, etc.
    """
    
    def fibonacci(self, n):
        if n < 0:
            raise ValueError("n debe ser no negativo")
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n):
        if n < 0:
            raise ValueError("n debe ser no negativo")
        return [self.fibonacci(i) for i in range(n)]
    
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        if n < 2:
            return []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(n + 1) if sieve[i]]
    
    def es_numero_perfecto(self, n):
        if n <= 1:
            return False
        suma = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                suma += i
                if i != n // i:
                    suma += n // i
        return suma == n

    def es_numero_armstrong(self, n):
        """
        Verifica si un número es un número de Armstrong.

        Args:
            n (int): Número a verificar

        Returns:
            bool: True si es un número de Armstrong, False en caso contrario
        """
        num_str = str(n)
        num_digitos = len(num_str)
        suma = sum(int(digito) ** num_digitos for digito in num_str)
        return suma == n
    
    def triangulo_pascal(self, filas):
        if filas < 0:
            raise ValueError("filas debe ser no negativo")
        if filas == 0:
            return []
        triangulo = [[1]]
        for i in range(1, filas):
            prev = triangulo[-1]
            nueva_fila = [1] + [prev[j-1] + prev[j] for j in range(1, i)] + [1]
            triangulo.append(nueva_fila)
        return triangulo
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("n debe ser no negativo")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    def mcd(self, a, b):
        a, b = abs(a), abs(b)
        while b:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))
    
    def es_cuadrado_magico(self, matriz):
        if not matriz or not matriz[0]:
            return False
        n = len(matriz)
        if any(len(row) != n for row in matriz):
            return False
        suma_objetivo = sum(matriz[0])
        return (
            all(sum(row) == suma_objetivo for row in matriz) and
            all(sum(matriz[row][col] for row in range(n)) == suma_objetivo for col in range(n)) and
            sum(matriz[i][i] for i in range(n)) == suma_objetivo and
            sum(matriz[i][n-1-i] for i in range(n)) == suma_objetivo
        )
