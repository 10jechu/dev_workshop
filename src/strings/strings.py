class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        texto = texto.lower().replace(" ", "")
        return texto == texto[::-1]
    
    def invertir_cadena(self, texto):
        resultado = ""
        for char in texto:
            resultado = char + resultado
        return resultado
    
    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        return sum(1 for char in texto if char in vocales)
    
    def contar_consonantes(self, texto):
        vocales = "aeiouAEIOU"
        return sum(1 for char in texto if char.isalpha() and char not in vocales)
    
    def es_anagrama(self, texto1, texto2):
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())
    
    def contar_palabras(self, texto):
        return len(texto.split())
    
    def palabras_mayus(self, texto):
        return " ".join([palabra.capitalize() for palabra in texto.split()])
    
    def eliminar_espacios_duplicados(self, texto):
        return " ".join(texto.split())
    
    def es_numero_entero(self, texto):
        texto = texto.strip()
        if not texto:
            return False
        if texto[0] == "-":
            texto = texto[1:]
        return texto.isdigit()
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for char in texto:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
            else:
                resultado += char
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        if not subcadena or len(subcadena) > len(texto):
            return []
        posiciones = []
        len_sub = len(subcadena)
        for i in range(len(texto) - len_sub + 1):
            if texto[i:i+len_sub] == subcadena:
                posiciones.append(i)
        return posiciones
