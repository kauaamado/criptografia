alfabeto = 'abcdefghijklmnopqrstuvwxyz'

class Utils:
    def __init__(self, texto):
        self.texto = texto
    def limpar_duplicatas(self):
        """Remove letras duplicadas (mantém a primeira ocorrência)."""
        self.texto = "".join(dict.fromkeys(self.texto))

    def limpar_espacos(self):
        """Remove espaços do texto."""
        self.texto = self.texto.replace(' ', '')

    def limpar(self):
        """Limpa o texto: minusculas, sem espaços, sem duplicatas."""
        self.texto = self.texto.lower()
        self.limpar_espacos()
        self.limpar_duplicatas()

        return self.texto