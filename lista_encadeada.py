from no import No



class Lista_encadeada:


    def __init__(self) -> None:
        self.inicio = None
        self.size = 0
        pass


    def inserir(self,valor,indice = None):
        if indice == None:
            indice = self.size

        # inserir no primeiro da lista
        if self.inicio == None:
            no = No(valor)
            self.inicio = no
            

        else:

            variavel_percorer = self.inicio
            if indice > self.size :
                return print(f'Essa lista não contem {indice} elementos')
            
            for elemento in range(0,indice-1):
                print(elemento)
                variavel_percorer = variavel_percorer.next
            
            no = No(valor)
            if indice == 0:
                no.next = self.inicio
                self.inicio = no
            else:
                no.next = variavel_percorer.next
                variavel_percorer.next = no

        self.size += 1
    def apagar(self,valor):

        # apagar o primeiro ou outro qualquer lugar
        variavel = self.inicio
        while variavel != None:

            apoio = variavel
            variavel = variavel.next

            if variavel == None:
                print(f'Não existe o elemento {valor} na lista')

            elif variavel.valor == valor:
                apoio.next = variavel.next
                self.size -=1
                break


    def mostrar(self):

        repetir = self.inicio
        print('[',end='')

        while repetir != None:

            print(repetir.valor,end='')
            if repetir.next != None:
                print(',',end='')

            repetir = repetir.next

        print(']')



