import argparse
from utilitarios import Utils

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
numeros = '1234567890'

def construir_parser():
    parser = argparse.ArgumentParser(
    description="Algoritmo de encriptação Cifra de César",
    epilog="GitHub: https://github.com/kauaamado/criptografia"
    )

    modo = parser.add_mutually_exclusive_group(required=True)
    modo.add_argument("-C", "--cifrar", action="store_const", help="Cifrar", dest="modo", const="cifrar")
    modo.add_argument("-D", "--decifrar", action="store_const", help="Decifrar", dest="modo", const="decifrar")
    modo.add_argument("-I", "--interativo", action="store_const", help="Modo Interativo", dest="modo", const="interativo")
    parser.add_argument("-t", "--texto", type=str, help="Texto")
    return parser

def main():
    parser = construir_parser()
    args = parser.parse_args()
    texto = args.texto

    if args.modo in ("cifrar", "decifrar") and (not args.texto):
        parser.error("nos modos -C/-D, as flags -t/--texto são obrigatórias")

    def inverter_alfabeto():
        """Inverte o alfabeto para a decriptação."""
        return alfabeto[::-1]

    def cifrar(texto):
        alfabeto_invertido = inverter_alfabeto()
        texto_cifrado = "".join(alfabeto_invertido[alfabeto.index(i)] for i in texto)
        return texto_cifrado

    def decifrar(texto):
        alfabeto_invertido = inverter_alfabeto()
        texto_pleno = "".join(alfabeto[alfabeto_invertido.index(i)] for i in texto)
        return texto_pleno
        

    if args.modo == "cifrar":
        resultado = cifrar(texto)
        print(resultado)
        #print(cifrar(args.texto))
    elif args.modo == "decifrar":
        print(decifrar(texto))
    elif args.modo == "interativo":
        print("Em construção...")

if __name__ == '__main__':
    main()