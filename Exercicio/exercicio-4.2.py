print('Calculadora')
print('+ adição')
print('- subtração')
print('* multiplicação')
print('/ divisão')
print('Pressione outra tecla para sair')

while True:

    op = input('Qual operação deseja fazer?')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))

    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}' .format(x, y, res))
        continue
    elif(op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}'.format(x, y, res))
        continue
    elif(op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}'.format(x, y, res))
        continue
    elif(op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}'.format(x, y, res))
        continue
    elif(op == 's'):
        break
    else:
        print('Operação invalida')



print('Encerrando o programa...')