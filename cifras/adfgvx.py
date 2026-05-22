# Algoritmo de encriptação ADFGVX

from utilitarios import Utils

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
numeros = '1234567890'

quadrado_de_polibio = [[], [], [], [], [], []] # linha, coluna

menu = {
    1: 'Encriptar',
    2: 'Desencriptar',
    3: 'Sair'}


def preencher_quadrado_de_polibio(chave_limpa, texto):
    print("[DEBUG] Chave limpa: " + chave_limpa)
    print("[DEBUG] Texto: " + texto)

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

def transposicao_colunar(chave_limpa, texto_substituido):
    # O enumerate foi usado para obter a posição original de cada letra da chave
    # enumerate('MARTE') gera: [(0, 'M'), (1, 'A'), (2, 'R'), (3, 'T'), (4, 'E')]
    colunas_com_indice = list(enumerate(chave_limpa))
    
    # Ordena alfabeticamente baseando-se na letra (que é o item [1] de cada tupla)
    # Resultado para 'MARTE': [(1, 'A'), (4, 'E'), (0, 'M'), (2, 'R'), (3, 'T')]
    colunas_com_indice.sort(key=lambda x: x[1])

    texto_cifrado_transposto = []
    tamanho_chave = len(chave_limpa)

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

def encriptar(chave, texto):
    
    chave = Utils(chave)
    texto = texto.lower()

    chave_limpa = chave.limpar()

    preencher_quadrado_de_polibio(chave_limpa, texto)

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

    texto_cifrado = transposicao_colunar(chave_limpa, texto_substituido)
    
    return texto_cifrado
        

while True:
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
            pass
        elif opcao == '3':
            print('Saindo...')
            break
    except ValueError:
        print('Opção inválida')
