menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do Deposito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print("Seu saldo atual é de: R$ ", saldo)

        else:
            print("Erro! O valor informado não é válido. Por favor, tente novamente")

    elif opcao == "s":
        valor_saque = float(input("Digite o valor do saque: "))

        saldo_insuficiente = valor_saque > saldo

        limite_insuficiente = valor_saque > limite

        saques_insuficientes = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("Operação inválida, saldo insuficiente")

        elif limite_insuficiente:
            print("Operação inválida, O valor do saque excede o limite.")

        elif saques_insuficientes:
            print("Operação falhou! Número máximo de saques excedido. ")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saques:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        print("\n================== EXTRATO =================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
