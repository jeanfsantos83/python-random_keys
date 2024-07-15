import random
import string

def gerar_codigo(tamanho=6):
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return codigo

def main():
    print("Gerador de Códigos de Verificação")
    print("-------------------------------")

    while True:
        print("Opções:")
        print("  1. Gerar código de verificação")
        print("  2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tamanho = int(input("Digite o tamanho do código (padrão=6): ") or 6)
            codigo = gerar_codigo(tamanho)
            print(f"Código de verificação gerado: {codigo}")
        elif opcao == "2":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
