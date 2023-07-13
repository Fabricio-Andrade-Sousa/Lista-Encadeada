from lista_encadeada import Lista_encadeada


lista = Lista_encadeada()
# lista.inserir(3)
# lista.mostrar()
# lista.inserir(10)
# lista.mostrar()
# lista.inserir(5)
# lista.inserir(7,2)
# lista.inserir(6,3)
# lista.inserir('i',4)
# lista.inserir(2,5)
# lista.inserir(10,0)
# lista.mostrar()
print(5*'-', 'Lista Encadeada', 5*'-')

while True:
    print(10*'-')
    print('0- sair')
    print('1- adcionar')
    print('2- remover')
    print(10*'-')
    escolha = int(input('escolha uma ação para a lista '))
    if escolha == 1:
        valor = int(input('valor: '))
        posicao = int(input('Posição da lista: '))
        lista.inserir(valor, posicao)

    elif escolha == 2:
        valor = int(input('valor: '))
        lista.apagar(valor)
    elif escolha == 0:
        break
    lista.mostrar()
