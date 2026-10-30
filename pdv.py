# Lista para guardar o histórico de cada compra
historico = []

print("=== SISTEMA DE PDV 67 AUTOMAÇÕES ===")

# Loop principal do programa
rodando = True

while rodando:
    print("\n--------------------------------")
    
    # 1. Entrada do valor
    valor_da_compra = float(input("Digite o valor da compra (ou 0 para sair): R$ "))

    # If utilizado para encerrar o programa caso o usuário digite o número 0
    if valor_da_compra == 0:
        rodando = False
        continue

    # Validação caso o numero digitado seja negativo, mostrando uma mensagem de aviso e pedindo para tentar novamente
    if valor_da_compra < 0:
        print("Aviso: O valor nao pode ser negativo! Tente novamente.")
        continue

    # 2. idade do cliente
    idade = int(input("Digite a idade do cliente: "))

    # Caso a idade seja negativa!
    if idade < 0:
        print("Aviso: A idade nao pode ser negativa! Tente novamente.")
        continue

    # 3. Regra 1: Desconto de idade para os maiorais
    if idade >= 65:
        desconto_idade = valor_da_compra * 0.20
        valor_com_desconto = valor_da_compra - desconto_idade
    else:
        valor_com_desconto = valor_da_compra

    # 4. Regra 2: Desconto por valor para os terrores do INSS
    if valor_com_desconto > 100:
        desconto_valor = valor_com_desconto * 0.10
        valor_final = valor_com_desconto - desconto_valor
    else:
        valor_final = valor_com_desconto

    cupom = input("Caso tenha um cupom de desconto, digite-o agora (ou pressione Enter para pular): ")

    if cupom == "FIDELIDADE10":
        # 5. Regra 3: Desconto por cupom
        desconto_cupom = valor_com_desconto * 0.10
        valor_final = valor_com_desconto - desconto_cupom
    else:
        valor_final = valor_com_desconto

    # Calcula quanto deu de desconto total nessa compra
    desconto_total_compra = valor_da_compra - valor_final

    # Exibe o valor final formatado com 2 casas decimais
    print(f"Valor final a pagar: R$ {valor_final:.2f}")

    # Guardando os dados da compra na lista de histórico: [original, desconto, final]
    compra = [valor_da_compra, desconto_total_compra, valor_final]
    historico.append(compra)

print("          RESUMO DO DIA           ")


# Variáveis para guardar as somas totais
total_compras = len(historico)
soma_bruto = 0.0
soma_descontos = 0.0
soma_final = 0.0


for item in historico:
    soma_bruto = soma_bruto + item[0]
    soma_descontos = soma_descontos + item[1]
    soma_final = soma_final + item[2]

# Resultado 
print(f"Quantidade de compras registradas: {total_compras}")
print(f"Total bruto: R$ {soma_bruto:.2f}")
print(f"Total de descontos concedidos: R$ {soma_descontos:.2f}")
print(f"Total final acumulado: R$ {soma_final:.2f}")
print("====")
print("Obrigado por utlizar o sistema de PDV 67 Automações, volte sempre!")