saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def aguardar_limpar_tela(tempo=2):
    from os import system
    from time import sleep

    sleep(tempo)
    system("cls") or None


def centralizar_titulo(titulo: str) -> str:
    print(titulo)
    print("*" * len(titulo), "\n")


def depositar():
    aguardar_limpar_tela()
    centralizar_titulo("Depósito")

    global saldo
    global numero_saques
    global extrato

    deposito = float(input("Valor a depositar R$"))

    while True:
        resposta_deposito = int(
            input(
                f"Confirmar o depósito de valor R${str(deposito).replace(".", ",")}\n[1] Sim [2] Não\n:"
            )
        )

        if resposta_deposito == 1:
            saldo += deposito
            numero_saques += 1
            extrato += f"Depositado R${str(deposito).replace(".", ",")}\n"
            print("Depósito concluído com sucesso...")
            break

        elif resposta_deposito == 2:
            print("Operação cancelada.")
            print("Retornando ao menu principal...")
            break

        else:
            print("Opção inválida. Por favor tente novamente...")

    retornar_menu_principal()


def sacar():
    aguardar_limpar_tela()
    centralizar_titulo("Saque")

    saque = float(input("Valor a sacar R$"))

    global saldo
    global numero_saques
    global extrato

    while True:
        resposta_saque = int(
            input(f"\nConfirmar o saque de R${str(saque).replace(".", ",")}?\n[1] Sim [2] Não\n:")
        )

        if resposta_saque == 1:
            if numero_saques <= LIMITE_SAQUES:
                if saldo >= saque and saque <= 500:
                    saldo -= saque
                    numero_saques += 1
                    extrato += f"Saque R${str(saque).replace(".", ",")}\n"
                    print("Saque concluído com sucesso...")
                    break

                elif saque > 500 and saldo > 500:
                    print(
                        'O limite por tentativa de saque é de R$500,00... Por favor tente novamente!"'
                    )
                    break

                else:
                    print("Você não possui saldo suficiente em conta...")
                    break
            else:
                print(
                    "Você atingiu o limite de saque diário. Por favor tente novamente no próximo dia..."
                )
                break

        elif resposta_saque == 2:
            print("Operação cancelada.")
            break

        else:
            print("Opção inválida. Por favor tente novamente...")
            aguardar_limpar_tela()

    retornar_menu_principal()


def ver_extrato():
    aguardar_limpar_tela()
    centralizar_titulo("Extrato")

    global saldo
    global extrato

    if extrato == "":
        print("Não foram realizadas movimentações")
    else:
        print(extrato, f"\nSaldo: R${str(saldo).replace(".", ",")}")
    
    retornar_menu_principal(4)


def acessar_menu():
    menu = """

    Sistema Bancário

    [1] Depósitar
    [2] Sacar
    [3] Extrato
    [0] Sair

    :
"""

    while True:
        opcao = input(menu)

        if opcao == "1":
            return depositar()
        elif opcao == "2":
            return sacar()
        elif opcao == "3":
            return ver_extrato()
        elif opcao == "0":
            print("Encerrando o sistema, aguarde...")
            break
        else:
            print("Opção inválida... Por Favor tente novamente!")

    aguardar_limpar_tela()
    print("Obrigado por utilizar nossos serviços. Volte sempre!")


def retornar_menu_principal(tempo=2):
    aguardar_limpar_tela(tempo)
    print("Retornando ao menu principal...")
    aguardar_limpar_tela()
    return acessar_menu()
