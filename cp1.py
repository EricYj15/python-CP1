# Menu do cabeçalho
print(46*'-')
print(5*'-','\033[0;30;41mSeja muito bem vindo a FRUTARIA ES\033[m',5*'-')
print(46*'-')
# Input de dados do usuário
nome = input('Digite o seu nome: ')
print()
endereco = input(f'{nome}, por favor, digite o seu endereço: ')
print()
ano = int(input(f'{nome}, diga o seu ano de nascimento: '))
idade = 2024 - ano
print()
# Descrição das frutas do dia
uva = 10.50
morango = 20.10
melancia = 15.40
banana = 2.75
maca = 4.50
print(f'{nome}, as frutas do dia são as seguintes: ')
print(42*'-')
print('|', 'Id', '|', f'{"Fruta":15s}', '|', f'{"R$/kg":15s}', '|')
print(42*'-')
print('|', ' 1', '|', f'{"Uva":15s}', '|', f'{uva:15.2f}', '|')
print('|', ' 2', '|', f'{"Morango":15s}', '|', f'{morango:15.2f}', '|')
print('|', ' 3', '|', f'{"Melancia":15s}', '|', f'{melancia:15.2f}', '|')
print('|', ' 4', '|', f'{"Banana":15s}', '|', f'{banana:15.2f}', '|')
print('|', ' 5', '|', f'{"Maçã":15s}', '|', f'{maca:15.2f}', '|')
print(42*'-')

#msg = '''
#-------------------------
#|Fruta     |    Preço/kg |
#--------------------------
#|Uva ----------- R$ 10.50|
#|Maçã ----------- R$ 5.55|
#--------------------------
#'''
#print(msg)

# Segundo input de dados do usuário

fruta = input(f'{nome}, digite o id da fruta que você deseja comprar? ')
peso = float(input('Digite a quantidade, em kg, da fruta que você deseja comprar: '))

var = True

if fruta == '1':
    valor = peso*uva
elif fruta == '2':
    valor = peso*morango
elif fruta == '3':
    valor = peso*melancia
elif fruta == '4':
    valor = peso*banana
elif fruta == '5':
    valor = peso*maca
else:
    print('Opção Inválida!')
    var = False

#print(valor)
if var == True:
# Calcular o frete
    frete = 4.50
    if valor <= 15:
        valor = valor + frete
        print(f'Você terá um acréscimo em sua compra de R${frete:.2f}')
    else:
        print('Estamos lhe dando uma isenção no frete!')

    #print(valor)

    # Calcular o desconto
    if idade > 60:
        valor = valor*0.95
        print('O(a) Sr(a) possui um desconto de 5%')

    print()
    print(f'Obrigado {nome}, sua compra ficou no valor de R${valor:.2f}, e será entregue no endereço: {endereco}.')