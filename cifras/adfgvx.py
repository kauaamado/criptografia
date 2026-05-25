# Algoritmo de encriptação ADFGVX

import argparse
from utilitarios import Utils

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
numeros = '1234567890'

menu = {
    1: 'Encriptar',
    2: 'Desencriptar',
    3: 'Sair'}

def construir_parser():
    parser = argparse.ArgumentParser(
    description="Algoritmo de encriptação ADFGVX",
    epilog="GitHub: https://github.com/kauaamado/criptografia"
    )

    modo = parser.add_mutually_exclusive_group(required=True)
    modo.add_argument("-E", "--encrypt", action="store_const", help="Encriptar", dest="modo", const="encriptar")
    modo.add_argument("-D", "--decrypt", action="store_const", help="Decriptar", dest="modo", const="desencriptar")
    modo.add_argument("-I", "--interactive", action="store_const", help="Modo Interativo", dest="modo", const="interativo")
    parser.add_argument("-k", "--key", type=str, help="Chave")
    parser.add_argument("-t", "--text", type=str, help="Texto")
    return parser

def main():
    parser = construir_parser()
    args = parser.parse_args()

    if args.modo in ("encriptar", "desencriptar") and (not args.key or not args.text):
        parser.error("nos modos -E/-D, as flags -k/--key e -t/--text são obrigatórias")

    def preencher_quadrado_de_polibio(chave_limpa):
        print("[DEBUG] Chave limpa: " + chave_limpa)

        conteudo_quadrado = "" + chave_limpa + alfabeto
        conteudo_quadrado = Utils(conteudo_quadrado).limpar()
        print(conteudo_quadrado)
        conteudo_quadrado = list(conteudo_quadrado)
        for letra in alfabeto[:10]:
            posicao_no_quadrado = conteudo_quadrado.index(letra)
            conteudo_quadrado.insert(posicao_no_quadrado + 1, numeros[alfabeto.index(letra)])

        print("[DEBUG] Quantidade de casas: " + str(len(conteudo_quadrado)))

        for i in range(6):
            for j in range(6):
                quadrado_de_polibio[i].append(conteudo_quadrado[i * 6 + j])

        return quadrado_de_polibio

    def exibir_quadrado_de_polibio(quadrado_de_polibio):
        for i in quadrado_de_polibio:
            print(i)

    def transposicao_colunar(chave, texto_substituido):
        # O enumerate foi usado para obter a posição original de cada letra da chave
        # enumerate('MARTE') gera: [(0, 'M'), (1, 'A'), (2, 'R'), (3, 'T'), (4, 'E')]
        colunas_com_indice = list(enumerate(chave))
    
        # Ordena alfabeticamente baseando-se na letra (que é o item [1] de cada tupla)
        # Resultado para 'MARTE': [(1, 'A'), (4, 'E'), (0, 'M'), (2, 'R'), (3, 'T')]
        colunas_com_indice.sort(key=lambda x: x[1])

        texto_cifrado_transposto = []
        tamanho_chave = len(chave)

        # Extrai as colunas usando fatiamento (slicing)
        for indice_original, _ in colunas_com_indice: # _ ignora o item da tupla, nesse caso, a letra.
        
            # O "pulo do gato": O fatiamento [indice_original :: tamanho_chave]
            # pega a letra no índice inicial e pula de N em N casas (onde N é o tamanho da chave).
            # Isso varre a coluna inteira de cima a baixo, independente de quantas linhas existam,
            # e lida automaticamente com colunas que terminam mais cedo.
            coluna_extraida = texto_substituido[indice_original :: tamanho_chave]

            # Usamos o método .append() para adicionar a coluna inteira na nossa lista
            texto_cifrado_transposto.append(coluna_extraida)

        # 4. Usar o método "".join() para unificar a lista de strings em um texto só
        texto_final = "".join(texto_cifrado_transposto)
    
        return texto_final

    def reverter_transposicao_colunar(chave_limpa, texto_cifrado):
        tamanho_chave = len(chave_limpa)
        tamanho_texto = len(texto_cifrado)

        # Rastrea a posição original e ordenar (mesmo passo da encriptação)
        colunas_com_indice = list(enumerate(chave_limpa))
        colunas_com_indice.sort(key=lambda x: x[1])

        # A Matemática do esqueleto das colunas singulares
        linhas_completas = tamanho_texto // tamanho_chave
        letras_sobrando = tamanho_texto % tamanho_chave

        # Descobre o tamanho de cada coluna na ordem ALFABÉTICA
        tamanhos_colunas = []
        for indice_original, _ in colunas_com_indice:
            # Se o índice original da coluna for menor que o número de letras sobrando,
            # ela fica nas primeiras posições da matriz, logo, é uma "coluna longa".
            if indice_original < letras_sobrando:
                tamanhos_colunas.append(linhas_completas + 1)
            else:
                tamanhos_colunas.append(linhas_completas)

        # Fatia o texto cifrado para separar as colunas
        colunas_extraidas = {}
        inicio = 0
        for i, (indice_original, _) in enumerate(colunas_com_indice):
            tamanho_dessa_coluna = tamanhos_colunas[i]
            fim = inicio + tamanho_dessa_coluna

            # Guardamos a fatia do texto associada ao seu índice original da chave
            colunas_extraidas[indice_original] = texto_cifrado[inicio:fim]
            inicio = fim

        # Lê o texto original linha por linha
        texto_substituido_recuperado = ""
        # O número máximo de linhas sempre será as completas + 1 (se houver resto)
        for linha in range(linhas_completas + 1):
            for i in range(tamanho_chave): # Percorre na ordem original da chave (0, 1, 2...)
                coluna_atual = colunas_extraidas[i]
                # Só adiciona a letra se a coluna tiver chegado até essa linha (evita erro nas casas vazias)
                if linha < len(coluna_atual):
                    texto_substituido_recuperado += coluna_atual[linha]

        return texto_substituido_recuperado

    def encriptar(chave, texto):
        chave_transposicao = chave.replace(' ', '')
    
        chave = Utils(chave).limpar()
        texto = texto.lower()


        chave_limpa = chave

        preencher_quadrado_de_polibio(chave_limpa)

        exibir_quadrado_de_polibio(quadrado_de_polibio)
    
        # Cifragem do texto
        texto_substituido = ""
        texto = texto.replace(' ', '')
    
        relacao = {
            0: 'A',
            1: 'D',
            2: 'F',
            3: 'G',
            4: 'V',
            5: 'X'
        }
    
        for letra in texto:
            for i in range(6):
                for j in range(6):
                    if quadrado_de_polibio[i][j] == letra:
                        texto_substituido += relacao[i]
                        texto_substituido += relacao[j]
                        break

        texto_cifrado = transposicao_colunar(chave_transposicao, texto_substituido)
    
        return texto_cifrado

    def desencriptar(chave, texto_cifrado):
        chave_transposicao = chave.replace(' ', '')

        chave = Utils(chave).limpar()
        chave_limpa = chave
    
        texto_substituido = reverter_transposicao_colunar(chave_transposicao, texto_cifrado)

        preencher_quadrado_de_polibio(chave_limpa)

        exibir_quadrado_de_polibio(quadrado_de_polibio)

        texto_pleno = ""
        relacao_inversa = {'A': 0, 'D': 1, 'F': 2, 'G': 3, 'V': 4, 'X': 5}

        limite = int(len(texto_substituido) - (len(texto_substituido) % 2))
        for i in range(0, limite, 2):
            linha = relacao_inversa.get(texto_substituido[i])
            coluna = relacao_inversa.get(texto_substituido[i + 1])
            if linha is not None and coluna is not None:
                texto_pleno += quadrado_de_polibio[linha][coluna]

        return texto_pleno
    
    if args.modo == "interativo":
        while True:
            quadrado_de_polibio = [[], [], [], [], [], []] # linha, coluna

            print('===========================================')
            print('Bem vindo ao algoritmo de cifragem ADFGVX')
            print('===========================================')
            for i in menu:
                print(i , '-', menu[i])
            print('===========================================')

            try:
                opcao = input('Escolha uma opção: ')

                print(opcao)

                if opcao == '1':
                    print('Encriptando...')

                    chave = input('Insira a chave: ')
                    texto = input('Insira o texto: ')

                    print(encriptar(chave, texto))
                elif opcao == '2':
                    print('Desencriptando...')

                    chave = input('Insira a chave: ')
                    texto_cifrado = input('Insira o texto cifrado: ')
                    texto_cifrado = texto_cifrado.replace(' ', '').upper()

                    print(desencriptar(chave, texto_cifrado))
                elif opcao == '3':
                    print('Saindo...')
                    break
            except ValueError:
                print('Opção inválida')

        print('===========================================')
        print('Obrigado por usar o algoritmo de cifragem ADFGVX')
        print('===========================================')

    if args.modo == "encriptar":
        quadrado_de_polibio = [[], [], [], [], [], []] # linha, coluna
        print(encriptar(args.key, args.text))

    if args.modo == "desencriptar":
        quadrado_de_polibio = [[], [], [], [], [], []] # linha, coluna
        print(desencriptar(args.key, args.text))

if __name__ == '__main__':
    main()
