menu = """

[d] Deposito
[s] Saque
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
        valor = float(input("digite o valor do deposito: "))
        
        if valor > 0:
            saldo += valor 
            extrato += f"Deposito: R$ {valor:.2f} \n"

        else:
            print ("Sua operacao falhou, o valor informado e invalido")

    elif opcao == "s":

        valor = float(input("informe valor para saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print ("Operacao invalida, saldo excedido")
        
        elif excedeu_limite:
            print ("Operacao invalida, limite excedido")

        elif excedeu_saques:
            print ("Operacao invalida, saque diario excedido")

        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque: R$ {valor:.2f} \n"
            numero_saques += 1

        else:
            print ("Valor invalido, tente novamente:")
        
    elif opcao == "e":
        print("extrato".center(50,"_"))
        print("Nao foram encontrado movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("_".center(50,"_"))

    elif opcao == "q":
        break
    else:
        print("operacao invalida, tente novamente")