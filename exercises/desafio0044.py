""" Escreva um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:

- A vista dinheiro/cheque: 10% de desconto
- A vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""

# Input: Recebendo o preço do produto e a condição de pagamento.
preco_normal = float(input("Digite o preço normal do produto (R$): "))
print("""
Escolha a condição de pagamento:
[ 1 ] À vista (dinheiro/cheque) - 10% de desconto
[ 2 ] À vista no cartão - 5% de desconto
[ 3 ] Em até 2x no cartão - preço normal
[ 4 ] 3x ou mais no cartão - 20% de juros
""")
opcao = int(input("Digite o número correspondente à condição de pagamento: "))

# Processing: Calculando o preço final com base na condição escolhida.
if opcao == 1:
    preco_final = preco_normal * 0.90  # 10% de desconto.
    print(f"Pagamento à vista (dinheiro/cheque). Valor final: R$ {preco_final:.2f}")
elif opcao == 2:
    preco_final = preco_normal * 0.95  # 5% de desconto.
    print(f"Pagamento à vista no cartão. Valor final: R$ {preco_final:.2f}")
elif opcao == 3:
    preco_final = preco_normal  # Preço normal.
    print(f"Pagamento em até 2x no cartão. Valor final: R$ {preco_final:.2f}")
elif opcao == 4:
    parcelas = int(input("Digite o número de parcelas (mínimo 3): "))
    if parcelas >= 3:
        preco_final = preco_normal * 1.20  # 20% de juros.
        valor_parcela = preco_final / parcelas
        print(f"Pagamento em {parcelas}x no cartão. Valor final: R$ {preco_final:.2f}")
        print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
    else:
        print("Número de parcelas inválido. Para esta opção, o mínimo é 3 parcelas.")
else:
    print("Opção inválida! Por favor, escolha uma condição de pagamento válida.")
