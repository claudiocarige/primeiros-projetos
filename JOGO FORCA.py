from random import randint 
import os 
from time import sleep


palavras = ['sapo','chave','tulipa','cargo','calote','visor','limão','rouba','boneca','natural','trigo','tomate','cagada','baby','fralde','calango','colheita','homem','tartaruga','elefante','peixe','balão']

pergunta = input('Gostaria de jogar FORCA?\nDigite "S" para SIM. :')

while pergunta == 'S' or pergunta =='s':#COMEÇA A RODAR O CODIGO
    i = randint(0,21) 
    palavra = palavras[i] 
    qt_letras = len(palavra) 
    cont = 0 
    letras_corretas = []
    l = 0
    os.system('cls')
    print('\nJOGO DA FORCA.')
    print('A palavra tem {} letras.'.format(qt_letras))
    while l != len(palavra):#
        letras_corretas.append(' ')
        #print('_ ', end='')
        l += 1
    letras_erradas = [] 
    letra = '' 
    palavra_certa_minuscula =''
    digite = ''
    letras_digitadas = []
    while cont < qt_letras: 
        if cont > 0:
            print('\nJOGO DA FORCA.')
            print('A palavra tem {} letras.'.format(qt_letras))
        print('Letras digitadas:  ', end="")
        for item in letras_digitadas:
            print('{} '.format(item), end="")
        print('\n')
        digite = input('\nDigite uma letra: ') 
        letra = digite.casefold()
        letras_digitadas.append(letra)
        if len(letra) == 1 and letra.isalpha() == True: 
            '''for item in palavra: 
                print('_ {}'.format(item), end='')''' 
            os.system('cls')
            if letra in palavra: 
                for pos, char in enumerate(palavra): 
                    if (char == letra): 
                        letras_corretas[pos] = letra 
                        setor = 0
                while setor < qt_letras: 
                    if letras_corretas[setor] == ' ': 
                        print('_ ', end='') 
                    else: 
                        print(letras_corretas[setor], end="") 
                    setor += 1         
            else: 
                letras_erradas.append(letra) 
                print('\nNão tem a letra "{}" na palavra: '.format(letra)) 
                setor =0
                while setor < qt_letras: 
                   if letras_corretas[setor] == ' ': 
                        print('_ ', end='') 
                   else:
                       print(letras_corretas[setor], end="") 
                   setor += 1 
        else: 
            print('Digite a letra novamente') 
            cont -= 1 
        cont += 1 
        palavra_certa = ''
        if cont > 2: 
            print('\n\nJá sabe qual a palavra?\n\n') 
            resp = input('Digite S para "Sim" e N para "Não": ') 
            if resp == 'S' or resp =='s': 
                palavra_certa = input('Digite a palavra: ') 
                palavra_certa_minuscula = palavra_certa.casefold()
                if palavra_certa_minuscula == palavra: 
                    print('\n\nVOCÊ ACERTOU!\n') 
                    print('A palavra certa é: {}'.format(palavra)) 
                    cont = qt_letras 
                    sleep(4.0)
                else: 
                    print('\nVOCÊ ERROU!') 
                    print('\nA palavra não é {}!'.format(palavra_certa_minuscula))
                    sleep(4.0)
            os.system('cls') 
        resp1 = ''
        if cont == qt_letras and palavra_certa_minuscula != palavra:
            for item in letras_corretas:
                resp1 = resp1 + item
            
            if resp1 == palavra:
                print('PARABENS!\n')
                print('VOCÊ COMPLETOU A PALAVRA. \n')
                print('A palavra é : {}'.format(resp1))
            else:
                print('TENTE NOVAMENTE!')
                print('A palavra era {}'.format(palavra))
            
    pergunta = input('\n\nAinda deseja jogar FORCA, Digite "S" ou "s" para jogar. :') 
    os.system('cls')