# Algoritmo de encriptação ADFGVX

from utilitarios import Utils

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
numeros = '1234567890'

quadrado_de_polibio = [[], [], [], [], [], []] # linha, coluna

menu = {
    1: 'Encriptar',
    2: 'Desencriptar',
    3: 'Sair'}

def encriptar(chave, texto):
    chave = Utils(chave)
    texto = texto.lower()

    chave_limpa = chave.limpar()

    print(chave_limpa)
    print(texto)

    conteudo_quadrado = "" + chave_limpa + alfabeto
    conteudo_quadrado = Utils(conteudo_quadrado).limpar()
    print(conteudo_quadrado)
    conteudo_quadrado = list(conteudo_quadrado)
    for letra in alfabeto[:10]:
        posicao_no_quadrado = conteudo_quadrado.index(letra)
        conteudo_quadrado.insert(posicao_no_quadrado + 1, numeros[alfabeto.index(letra)])

    print("Quantidade: " + str(len(conteudo_quadrado)))

    print("Quadrado de polibio")

    for i in range(6):
        for j in range(6):
            quadrado_de_polibio[i].append(conteudo_quadrado[i * 6 + j])

    for i in quadrado_de_polibio:
        print(i)
    
    # Cifragem do texto
    cifrado = ""
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
                    cifrado += relacao[i]
                    cifrado += relacao[j]
                    break

    print(cifrado)
        

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
            
            encriptar(chave, texto)
        elif opcao == '2':
            pass
        elif opcao == '3':
            print('Saindo...')
            break
    except ValueError:
        print('Opção inválida')
