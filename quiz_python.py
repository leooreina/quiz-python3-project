# coding: utf-8

# Importação de módulo para encerrar o programa caso o usuário perca:

import sys

# Dicionários com as frases, lacunas, respostas_certas por dificuldade:

frases_lacunas_respostas_por_dificuldade = {
    'FACIL': {
        'frase': '''        Em python temos quatro tipos de valores:
        Para um valor inteiro, utilizamos __1__ , para um número flutuante
        podemos usar um __2__ . O do tipo __3__ só pode ser true ou false.
        Além disso, o mais usado são as strings, que são usadas como  __4__ .''',

        'lacunas': ['__1__', '__2__', '__3__', '__4__'],

        'respostas_certas': ['int', 'float', 'bool', 'str']
    },
    'MEDIO': {
        'frase': '''        Em python, os operadores matemáticos são utilizados
        para fazer adições, utilizando o sinal __1__ , para fazer subtrações
        com o __2__ , além de __3__ para multiplicações e __4__ para divisões.
        Temos também operações de divisão sem resto, chamada divisão inteira.
        Para isso usamos __5__ . Se nos for necessário saber o resto de uma divisão
        usamos o sinal de __6__ .''',

        'lacunas': ['__1__', '__2__', '__3__', '__4__', '__5__', '__6__'],

        'respostas_certas': ['+', '-', '*', '/', '//', '%']
    },
    'DIFICIL': {
        'frase': '''        Em python temos estruturas condicionais e de repetições.
        Em relação as condicionais, as mais conhecidas são __1__ e __2__ para indicar
        duas possibilidades de uma ação. Porém podemos utilizar o __3__ também, caso
        precise de mais do que duas opções. Já nas estruturas de repetições, para
        repetições finitas usamos: " __4__ valor in __5__ (começo, final):".
        Além disso, podemos também utilizar contadores para fazer contagens com variáveis. Para isso,
        iniciamos um variável qualquer como "contador = __6__ " e dentro do loop de repetição fazemos ela
        receber ela mesma + 1, usando assim "contador __7__ 1". Se estivermos interessados em loops
        infinitos de repetição, podemos usar o __8__ . Porém, cuidado, utilizando o comando __9__ para parar
        o loop e evitar que ele continue acontecendo para sempre.''',

        'lacunas': ['__1__', '__2__', '__3__', '__4__', '__5__', '__6__', '__7__', '__8__', '__9__'],

        'respostas_certas': ['if', 'else', 'elif', 'for',
                             'range', '0', '+=', 'while', 'break']
    }
}


# Boas vindas, início do jogo e instruções:


print('\033[35m-\033[m'*15, end="")
print('\033[34m VAMOS JOGAR O JOGO DA ADVINHAÇÃO '
      '\033[m', '\033[35m-\033[m'*15, '\n')
print('''\033[7mInstruções: Você receberá uma frase com lacunas\033[m
\033[7mpara serem preenchidas. Só será passado para a próxima\033[m
\033[7mlacuna quando a lacuna anterior obter a resposta correta.\033[m
\n\033[32mO nivel facil possui 4 lacunas e uma frase.\033[m
\n\033[33mO nivel medio possui 6 lacunas e uma frase.\033[m
\n\033[31mO nivel dificil possui 9 lacunas e uma frase.\033[m
\n''')
print('\033[35m-\033[m'*15, end="")
print('\033[34m BOA SORTE!\033[m ', '\033[35m-\033[m'*15, '\n')


# Usuário seleciona a dificuldade:

dificuldades = ['FACIL', 'MEDIO', 'DIFICIL']


def get_dificuldade():
    """Pergunta a dificuldade para o usuário que, caso
    não esteja nas possíveis, retornará a própria função.
    Se a dificuldade selecionada estiver nas possíveis
    retornará a dificuldade selecionada.
    """
    dificuldade = str(input(f'''Por favor, escolha uma dificuldade para o quiz:
\n        \033[32m|{dificuldades[0]:>8}|\033[m
\n        \033[33m|{dificuldades[1]:>8}|\033[m
\n        \033[31m|{dificuldades[2]:>8}|\033[m \n''')).upper().strip()
    if dificuldade not in dificuldades:
        print("Valor inválido! Tente novamente.")
        return get_dificuldade()
    else:
        print(f'\nVocê selecionou a dificuldade \033[34m {dificuldade}! \033[m')
        return dificuldade


nivel = get_dificuldade()


# Usuário selecionando o número de tentativas:

def get_tentativas():
    """Pergunta o número de tentativas por lacuna que o
    usuário deseja e retorna o número dado.
    """
    tentativas = int(input('\n\033[35mCom quantas tentativas por lacuna você deseja jogar?\033[m\n'))
    return tentativas


num_tentativas = get_tentativas()


# Localizando as frases, lacunas e respostas_certas de acordo com o nível escolhido.

def procura_frase_lacunas_respostas_dicionario():
    """Esta função retorna a frase, as lacunas e as respostas
    correspondentes para o nível selecionado pelo usuário.
    """
    frase = frases_lacunas_respostas_por_dificuldade[nivel]['frase']
    lacunas = frases_lacunas_respostas_por_dificuldade[nivel]['lacunas']
    respostas_certas = frases_lacunas_respostas_por_dificuldade[nivel]['respostas_certas']
    return frase, lacunas, respostas_certas


# Divide a frase:

def dividir_frase():
    """Esta função chama a função 'procura
    _frase_lacunas_respostas_dicionario()',
    divide a frase e retorna a frase dividida.
    """
    frase, lacunas, respostas_certas = procura_frase_lacunas_respostas_dicionario()
    frase_dividida = frase.split(' ')
    return frase_dividida


# Mostra a frase para o usuário:

def linha_e_frase(mensagem):
    """Esta função serve para imprimir
    uma mensagem (como a frase com as lacunas)
    entre duas linhas(uma na parte superior e
    outra na parte inferior).

    Argumento: mensagem - qualquer mensagem que
    pode ser imprimida.
    """
    print('\033[35m-\033[m'*80)
    print(f'\033[34m{mensagem}\033[m')
    print('\033[35m-\033[m'*80)


# Funcionamento do jogo, verifica se a resposta está correta e troca as respostas certas pela lacuna correspondente.
# Se o número de respostas erradas for igual ao número de tentativas, o jogo encerra e o usuário perde.

def esqueleto_jogo():
    """ 1) chama as funções:
    'procura_frase_lacunas_respostas_dicionario()'
    'dividir_frase()'

    2) Em seguida, verifica por cada lacuna a resposta
    do usuário. Caso esteja errada, soma um ao
    número de respostas erradas. Se o erro continuar
    acontecendo até atingir o número de tentativas
    selecionadas pelo usuário, o programa finaliza.

    3) Se as respostas dadas pelo usuário forem corretas,
    para cada lacuna será imprimido uma mensagem de resposta
    certa e será feito os passos a seguir:

    'posicao' -- acha a posição da lacuna na frase dividida
    'excluindo' -- exclui a lacuna na posicao
    'inserindo' -- insere a resposta certa na posicao
    'juntando' -- junta a frase dividida
    Por fim, imprime a frase com a lacuna preenchida para o
    usuário.
    """
    # 1):
    frase, lacunas, respostas_certas = procura_frase_lacunas_respostas_dicionario()
    frase_dividida = dividir_frase()
    # 2):
    for espaco in range(0, len(lacunas)):
        resposta = str(input(f'Qual a resposta para {lacunas[espaco]}?'))
        respostas_erradas = 0
        while resposta != (respostas_certas[espaco]) and num_tentativas > respostas_erradas:
            respostas_erradas += 1
            if respostas_erradas == num_tentativas:
                linha_e_frase(mensagem='        \033[34mVOCÊ PERDEU! PROGRAMA FINALIZADO.\033[m')
                sys.exit()
            linha_e_frase(mensagem='     \033[0;31mRESPOSTA ERRADA! Tente novamente.\033[m     ')
            resposta = str(input(f'Você tem mais {num_tentativas - respostas_erradas} tentativa(s). Qual a resposta para {lacunas[espaco]}?'))
        # 3):
        linha_e_frase(mensagem='     \033[0;36mRESPOSTA CORRETA!\033[m     ')
        posicao = frase_dividida.index(lacunas[espaco])
        excluindo = frase_dividida.pop(posicao)
        inserindo = frase_dividida.insert(posicao, respostas_certas[espaco])
        juntando = ' '.join(frase_dividida)
        linha_e_frase(mensagem=juntando)


# Ao completar todas as lacunas, o usuário termina o quiz e mostra mensagem final:

def game_over():
    """Chama a função linha_e_frase para imprimir a mensagem
    final do jogo.
    """
    linha_e_frase(mensagem='VOCÊ CONSEGUIU! Fim de jogo. Volte sempre.')


# Roda o jogo:

def rodando_jogo():
    """Chama as funções importantes para rodar o jogo."""
    frase, lacunas, respostas_certas = procura_frase_lacunas_respostas_dicionario()
    linha_e_frase(mensagem=frase)
    esqueleto_jogo()
    game_over()


rodando_jogo()
