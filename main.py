# 1 - imports / bibliotecas

# 2 - Classes

# 3 - metodos e funções = def => definition = definição

def print_hi(name):

    print(f'Hi, {name}')

def calcular_aula_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2

def calcular_area_do_triagulo(largura , comprimento):
    return largura * comprimento / 2

def contargem_progressiva(fim):
    for numero in range (fim): # repetir o bloco de zero até o fim
        print(numero) # exibir o numero


def apoiar_candidato(nome, vezes):
    for numero in range (vezes):
        # contador = numero + 1
        # print(f'{contador} - {nome}')


        # outra forma
        if numero < 9:
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1, '-', nome)




# estrutura de identificação / execução de script
if __name__ == '__main__':
    print_hi('Luis')

    # chamar a função de cálculo da área do retangulo
    resultado = calcular_aula_do_retangulo(4,4)
    print(f'A área do retângulo é de {resultado} m²')

    # chamar a função de cálculo da área do quadrado
    resultado = calcular_area_do_quadrado(5)
    print(f'A área do quadrado é de {resultado} m²')

    # chamar a função de cálculo da área do triângulo
    resultado = calcular_area_do_triagulo(7, 7)
    print(f'A área do triângulo é de {resultado} m²')

    # executar uma contagem progressisa
    contargem_progressiva(11)

    # exibir o nome do candidato várias vezes
    apoiar_candidato('Fake', 100)