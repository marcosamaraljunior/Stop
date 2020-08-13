#!/usr/env pyhton3
import ast,sys,argparse,os

# --------- HELP ------------
parser = argparse.ArgumentParser(description='teste arg')
parser.add_argument('--temas', "-t",required=False)
parser.add_argument('--letra', "-l",required=False)
argumentos = parser.parse_args()

letra_escolhida = ''

banner = '              #___________________________________________________________#\r\n'
banner += '             |  ____ _____ ___  ____     ____ _   _ _____    _  _____    |\r\n'
banner += '             | / ___|_   _/ _ \|  _ \   / ___| | | | ____|  / \|_   _|   |\r\n'
banner += '             | \___ \ | || | | | |_) | | |   | |_| |  _|   / _ \ | |     |\r\n'
banner += '             | ######################################################### |\r\n'
banner += '             |  ___) || || |_| |  __/  | |___|  _  | |___ / ___ \| |     |\r\n'
banner += '             | |____/ |_| \___/|_|      \____|_| |_|_____/_/   \_\_|     |\r\n'
banner += '             #-----------------------------------------------------------#\r\n'

def exibir_banner():
    print(banner)

def exibir_temas(temas_argumento):
    print('[STOP CHEAT] - ESCOLHA OS TEMAS \r\n\r\n')


    arquivo_temas = open('temas.txt','r')
    lista_temas = arquivo_temas.read()
    arquivo_temas.seek(0)
    
    temas = arquivo_temas.readlines()

    if len(temas_argumento) > 0:
        for tema in temas:
            tema = tema.lower()
            for escolhido in temas_argumento:
                if escolhido in tema:
                    print(tema)
    else:
            print(lista_temas)
  #Transforma a lista em Dicionarios (ID, Tema)

def buscar_todos_temas():
    arquivo_temas = open('temas.txt','r')
    lista_temas = arquivo_temas.read()
    return  ast.literal_eval(lista_temas)




def get_temas_argumento():
    if argumentos.temas:
        return argumentos.temas.split(',')
    else:
        return []

def get_letra_argumento():
    if argumentos.letra:
        return argumentos.letra
    else:
        return []


def escolher_temas():
    choosed = input('Escolha os temas da rodada a patir dos numeros separando-os por virgulas ","\r\n IDs ->  ')
    return choosed.split(',')

def escolher_letra():
    return input('Escolha a letra da rodada -> ')


def exibir_repsostas(temas, letra):
    print('\r\n\r\n')

    # Para cada tema
    # Abrir o Arquivo do tema
    # Buscar a Linha correspondente a Letra da Rodada.
    # Printar se existir.

    for tema in temas:
        path = tema.replace(' ','_')
        path = path.lower()
        lista = open(f'temas/{path}/lista.txt')
        resposta = lista.readlines()
        
        for res in resposta:
            if f'{letra.upper()}:' in res:
                print(f'[{tema}] : {res[3:len(res)]}')



def main():

    exibir_banner()

    id_temas_escolhidos =[]
    temas_escolhidos =[]

    temas_argumento = get_temas_argumento() # RETORNA OS temas ESCOLHIDOS POR ARGUMENTOS EM UM ARRAY
    temas = buscar_todos_temas() # Retorna um array de dicionarios (ID,TEMA)
    
    if len(temas_argumento) > 4 or len(temas_argumento) == 0:
        exibir_temas(temas_argumento)
        id_temas_escolhidos = escolher_temas() # DEIXA O USUARIO ESCOLHER OS TEMAS POR ID
    else:
        for(key,value) in temas.items(): # Para cada (ID, TEMA) na lista de temas.
            for palavra in value.lower().split(' '): # Para cada palavra do tema
                if(palavra in temas_argumento): # Se a palavra for igual a algum tema escolhido por argumento
                    id_temas_escolhidos.append(key) # Adicione o ID do tema na lista dos Ids escolhidos

    letra = get_letra_argumento()  # Pega a letra do argumento.
    if(letra):
        letra_escolhida = letra # Se houver argumento, use-o
    else:
        letra_escolhida = escolher_letra() # Se nao, permita que o usuario escolha uma letra.

    for id in id_temas_escolhidos:
        temas_escolhidos.append(temas.get(id)) #Adiciona a Lista o nome do tema correspondente ao ID.


    exibir_repsostas(temas_escolhidos,letra_escolhida)


main()



