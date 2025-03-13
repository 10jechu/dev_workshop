import pytest
from src.strings.strings import Strings

class TestStrings:
    def setup_method(self):
        self.strings = Strings()
    
    def test_es_palindromo(self):
        assert self.strings.es_palindromo("ana") is True
        assert self.strings.es_palindromo("reconocer") is True
        assert self.strings.es_palindromo("Anita lava la tina") is True
        assert self.strings.es_palindromo("sigmotoa") is False
        assert self.strings.es_palindromo("mundo") is False
        assert self.strings.es_palindromo("") is True
    
    def test_invertir_cadena(self):
        assert self.strings.invertir_cadena("hola") == "aloh"
        assert self.strings.invertir_cadena("Python") == "nohtyP"
        assert self.strings.invertir_cadena("sigmotoA") == "Aotomgis"
        assert self.strings.invertir_cadena("") == ""
        assert self.strings.invertir_cadena("a") == "a"
    
    def test_contar_vocales(self):
        assert self.strings.contar_vocales("sigmotoa") == 4
        assert self.strings.contar_vocales("murcielago") == 5
        assert self.strings.contar_vocales("rhythm") == 0
        assert self.strings.contar_vocales("AeIoU") == 5
        assert self.strings.contar_vocales("") == 0
    
    def test_contar_consonantes(self):
        assert self.strings.contar_consonantes("sigmotoa") == 4
        assert self.strings.contar_consonantes("Python") == 5
        assert self.strings.contar_consonantes("aeiou") == 0
        assert self.strings.contar_consonantes("PythOn") == 5
        assert self.strings.contar_consonantes("") == 0
    
    def test_es_anagrama(self):
        assert self.strings.es_anagrama("roma", "amor") is True
        assert self.strings.es_anagrama("listen", "silent") is True
        assert self.strings.es_anagrama("ekans", "sneak") is True
        assert self.strings.es_anagrama("Dormitory", "Dirty room") is True
        assert self.strings.es_anagrama("hello", "world") is False
        assert self.strings.es_anagrama("python", "typhons") is False
    
    def test_contar_palabras(self):
        assert self.strings.contar_palabras("Hola mundo") == 2
        assert self.strings.contar_palabras("Python es divertido") == 3
        assert self.strings.contar_palabras("  dev with sigmotoa    ") == 3
        assert self.strings.contar_palabras("") == 0
    
    def test_palabras_mayus(self):
        assert self.strings.palabras_mayus("hola mundo") == "Hola Mundo"
        assert self.strings.palabras_mayus("sigmotoa es genial") == "Sigmotoa Es Genial"
        assert self.strings.palabras_mayus("Hola Mundo") == "Hola Mundo"
        assert self.strings.palabras_mayus("  hola  mundo  ") == "  Hola  Mundo  "
        assert self.strings.palabras_mayus("") == ""
    
    def test_eliminar_espacios_duplicados(self):
        assert self.strings.eliminar_espacios_duplicados("Hola  mundo") == "Hola mundo"
        assert self.strings.eliminar_espacios_duplicados("  sigmotoa   es   genial  ") == " sigmotoa es genial "
        assert self.strings.eliminar_espacios_duplicados("Hola mundo") == "Hola mundo"
        assert self.strings.eliminar_espacios_duplicados("") == ""
    
    def test_es_numero_entero(self):
        assert self.strings.es_numero_entero("123") is True
        assert self.strings.es_numero_entero("-456") is True
        assert self.strings.es_numero_entero("12.34") is False
        assert self.strings.es_numero_entero("-0.67") is False
