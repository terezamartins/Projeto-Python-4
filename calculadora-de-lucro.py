# Calculadora de Lucro
import time

print('=' * 30)
print('CALCULADORA DE LUCRO')
print('=' * 30)

produto = str(input('Qual produto você gostaria de comprar? '))
preco_compra = float(input('Digite o preço de compra do produto: R$'))
preco_venda = float(input('Digite o preço de venda: R$'))
custos_adicionais = float(input('Digite os custos adicionais (opcional): R$'))
quantidade = int(input('Digite a quantidade de produto que será comprada: '))

# Calculando o lucro líquido
lucro = (preco_venda * quantidade) - ((preco_compra + custos_adicionais) * quantidade)

#Calculando margem de lucro
margem_lucro = (lucro / (preco_venda * quantidade)) * 100
print('=' * 30)
print('CALCULANDO O LUCRO...')
print('=' * 30)
time.sleep(2)
print(f'O lucro do produto {produto} é de R${lucro}, com uma margem de lucro de {margem_lucro}%.')