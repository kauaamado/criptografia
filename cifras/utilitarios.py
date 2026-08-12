import re
from unidecode import unidecode

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
numeros = '1234567890'

class Alfabeto:
    def __init__(self, texto, alfabeto):
        self.texto = texto
        self.alfabeto = alfabeto

    def validar(self):
        """Valida se o texto contém apenas letras do alfabeto."""
        for letra in self.texto:
            if letra not in self.alfabeto:
                raise ValueError(f"Caractere inválido: {letra}")
        return True
    
    def limpar_duplicatas(self):
        """Remove letras duplicadas (mantém a primeira ocorrência)."""
        self.texto = "".join(dict.fromkeys(self.texto))
        return self.texto

    def limpar_espacos(self):
        """Remove espaços do texto."""
        self.texto = self.texto.replace(' ', '')
        return self.texto

    def limpar_acentos_e_especiais(self):
        """Remove acentos e caracteres especiais."""
        self.texto = unidecode(self.texto)
        return self.texto

    def limpar_pontos_e_simbolos(self):
        """Remove pontuação e simbolos."""
        self.texto = re.sub(r'[^a-zA-Z\s]', '', self.texto)
        self.texto = re.sub(r'\s+', ' ', self.texto).strip()
        return self.texto

    def limpar(self):
        """Limpa o texto: minusculas, sem espaços, sem duplicatas."""
        self.texto = self.texto.lower()
        self.limpar_espacos()
        self.limpar_duplicatas()
        self.limpar_acentos_e_especiais()
        self.limpar_pontos_e_simbolos()
        
        return self.texto

class Utils(Alfabeto):
    def __init__(self, texto, alfabeto):
        super().__init__(texto, alfabeto)
        self.alfabeto = alfabeto

    def menu():
        """Exibe o menu de opções."""
        menu = {
            '1': 'Cifrar',
            '2': 'Decifrar',
            '3': 'Sair'
        }
        return menu