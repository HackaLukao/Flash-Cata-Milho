# The Game  
import random 
import time 

#                          INICIALIZAÇÃO DAS VARIÁVEIS 

qtd_sorteios = 5 # Quantidade de sorteios, ou seja, quantas letras, numeros... que irão aparecer na rodada (cada player joga 1 partida, todos os players jogam uma seção que é sempre 1). Esta variável é inicializada com 5, porém poderá ser editada pelo usuário eventualmente. 
lista_letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]  # Lista com todas as letras do alfabeto brasileiro
lista_palavras = ["Balacobaco", "Birosca", "Bugiganga","Bulhufas","Chumbrega", "Espelunca", "Faniquito","Galalau","Gororoba","Mequetrefe", "Mixuruca", "Sacripanta", "Salamaleque", "Serelepe", "Songamonga", "Tribufu", "Urucubaca", "Xexelento", "Ziquizira"] # Lista com palavras a serem soretadas
lista_sentenças = ["Trazei três pratos de trigo para três tigres tristes comerem","A Iara agarra e amarra a rara arara de Araraquara","Toco preto, porco fresco, corpo crespo", "Teto sujo, chão sujo", "Caixa de graxa grossa de graça", "Casa suja, chão sujo. Chão sujo, casa suja", "Um tigre, dois tigres, três tigres", "Atrás da porta torta tem uma porca morta","O gato fugiu pro mato e pegou carrapato no ato", "Luzia lustrava o lustre listrado, o lustre listrado luzia", "Chega de cheiro de cera suja", "Bagre branco, branco bagre","Fia, fio a fio, fino fio, frio a frio", "Uma trinca de trancas trancou Tancredo", "Bote a bota no bote e tire o pote do bote"] # Lista com trava-línguas que serão sorteadas
vetor_tempo_rodada = []    # Lista com todos os tempos_uma_rodad
players = []  # Lista que armazena os nomes dos players
placar = []  # Lista que armazena o tempo total de jogo de cada player
qtd_jogadores = 2 # Quantidade de jogadores, ou seja, quantas partidas terão (uma partida apenas 1 player joga). Tal variável é inicializada em 2, porém poderá ser editada pelo usuário. 

# ----------------------------------------------------------------------------------------------------------------------
print(""" \u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1

\t\t\t\t\u221E \U0001D405 \U0001D40B \U0001D400 \U0001D412 \U0001D407  \U0001D402 \U0001D400 \U0001D413 \U0001D400  \U0001D40C \U0001D408 \U0001D40B \U0001D407 \U0001D40E \u231B

 \u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1\u26A1

""")
input("\t\t\t\t   Tecle enter para entrar ")
while True:                 # MENU PRINCIPAL        # Enquanto os condicionais do Menu forem verdadeiros, executa-se os comandos do jogo. 
    print("""
    \t\t\t\t> > > \U0001F31F  MENU \U0001F31F  < < < 
    
Escolha um comando: 
1 \u2794 \U0001F3AE Jogar
2 \u2794 \U0001F527 Alterar configurações do jogo
3 \u2794  \U0001F5CE Sobre o Jogo
4 \u2794 \u274C Sair
    """)
    opção = int(input("Escolha uma opção: "))   # Declara a variável opção que será testada nas condicionais do While True do Menu
    if opção == 1:          # 1° OPÇÃO DO MENU                    # Testa se a variável opção contém o valor 1 
        for i in range(0,qtd_jogadores,1): # Repete de 0 até a quantidade de jogadores pré-definida, ou definida pelo usuário
            i = i + 1 # Incrementa +1 ao i, que por sua vez será o índice que aparecerá na tela do jogador (str(i))
            players.append(input("\n\U0001F582  Digite o nome do jogador ["+ str(i) +"]: ")) # Adiciona ao final da lista players o nome do jogador digitado, isso é feito até a quantidade de jogadores pré-definida ou editada pelo usuário
            continue # Continua o laço de repetição até a Quantidade de Jogadores 
        print("\nProcessando...")
        time.sleep(1) # Congela o processamento pelo tempo do parâmetro
        print("\n\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC\u25BC \n")
        print("""\U0001F5F8  Escolha o quais tipos de variáveis deseja sortear:
        1 \u2794  Letras  \u1D43 \u1D47 \u1D9C
        2 \u2794  Números  \u00B9 \u00B2 \u00B3
        3 \u2794  Palavras  \U0001F5E8
        4 \u2794  Sentenças  \U0001F5E3""")
        modelo_jogo = int(input("\nTecle a opção correspondente a escolhida: ")) #Escolha da opcao do menu
        print("\n\n \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \U0001F3C1 \n\n")
        while True: # Estrutura de repeticao condicional que permanece em loop ate que receba-se um input que retorne false (opcao diferente de 1, 2, 3, 4)
            if modelo_jogo == 1: #Letras
                for i in range(0,qtd_jogadores,1): # Estrutua de repeticao responsavel por repetir o script de jogo dos players(linhas 53 - 73) para o numero de participantes inicializado
                    print("\n \U0001F6A9 Agora é sua vez ",players[i],", boa sorte! Digite as Letras que aparecerem o mais rápido que conseguir.\n", sep='') # Printa a tela do usuário que está no indice i da lista players que agora é a vez dele(a). O sep separa os objetos dentro do print, nosso não separa com nada.  
                    input("\t\t\t \u26A0  Tecle Enter p/ começar... \u26A0\t")  # ador tecle enter para prosseguirEspera um enter para continuar o processamento
                    for i in range(3,0,-1): # Laco de repeticao para contagem re # Fará a contagem regressiva que aparecera depois do player[1] teclar enter demontrando estar preparado. Irá de 3 até 1, com incremento de -1. 
                        print(i) # Printa o índice i 
                        time.sleep(0.5)  # Congela o processamento pelo tempo do parâmetro, com objetivo de criar uma melhor experiência do usuário
                    print("Goooo!!\n")       
                    for i in range(0,qtd_sorteios,1): # Estrutura de repetição de 1 rodada, que repetirá de 0 à quantidade de sorteios pré-definida 
                        sorteio = random.choice(lista_letras) # Sorteia aleatóriamente um elemento da lista "lista_letras" e guarda na variável sorteio 
                        tempo_antes = time.time() # Declara o tempo_antes de digitar uma variável, com o valor da time.time()
                        val_letra = input("["+ sorteio +"] = ") # Printa na tela do usuário a letra sorteada e espera um input do sipo str que será guardado na val_letra
                        while val_letra != sorteio: # Testa se o valor em val-letra é diferente que o valor sortead, enquanto for diferente será pedido a digitação correta 
                            val_letra = input("[" + sorteio + "] = ") # Printa na tela do usuário a letra sorteada e espera um input do sipo str que será guardado na val_letra
                            continue # Continua o laço de repetição 
                        tempo_depois = time.time() # Declara o tempo_depois com o valor guardado em time.time() após digitar uma variável
                        tempo_uma_rodada = tempo_depois - tempo_antes  # Declara o tempo_uma_rodada com a diferença entre os valores guardados na variável tempo_antes, tempo_depois. Esse será o tempo de digitação de uma variável do sorteio. 
                        vetor_tempo_rodada.append(tempo_uma_rodada)  # Adiciona ao final da lista vetor_tempo_rodada = lista que armazena (todos os tempos_uma_rodada (digitação de uma variável sorteada)) de um player. O append adiciona ao final dessa lista o tempo de digitação.
                        tempo_partida = 0  # Zera a variável tempo_partida, para que esta armazene o tempo da próxima partida. O tempo_partida é a soma dos 'tempos_uma_rodada' que um player demorou para digitar cada letra, numero ou sentença... 
                    for i in range(len(vetor_tempo_rodada)): # Fará a Soma dos tempos_uma_rodada de 1 a len(vetor_tempo_rodada) vezes.
                        tempo_partida = tempo_partida + vetor_tempo_rodada[i]  # Armazena em tempo_partida o incremento tempo_partida e soma o valor guardado na posição i na lista vetor_tempo_rodada
                    vetor_tempo_rodada.clear() # Limpa a lista tempo uma rodada, para esta receber os valores da próxima partida com n rodadas 
                    placar.append(round(tempo_partida, 2)) # Adiciona ao final da lista placar o valor armazenado em tempo partida, com duas casas decimais. Cada índice dessa lista é um player, uma vez que eles são respectivos, desde a lista players. 
                print("\nE o(a) vencedor(a) foi...  \n")
                time.sleep(2) 
                print("\U0001F914\U0001F914\U0001F914\n") 
                time.sleep(1) 
                print("\t\t\t  >>> \U0001F3C6 >>> RANKING <<< \U0001F3C6 <<<\n")
                for i in range(len(placar)): # Estrutura de repetição que repetira os comandos len placar vezes, para formar o ranking
                    tempo_minimo_vencedor = min(placar) # Declara o tempo_minimo_vencedor com o valor minimo da lista placar
                    ind_vencedor = placar.index(tempo_minimo_vencedor) # Armazena na var. ind_vencedor a posição em que o tempo_minimo_vencedor se encontra na lista placar
                    vencedor = players[ind_vencedor] # Armazena na var. Vencedor o nome do player localizado na posição ind_vencedor da lista players. Este será o player com o tempo minimo armazenado na variavel tempo_minimo_vencedor
                    i = i + 1 # Incrementa 1 em i. Este valor irá corresponder a colocação de cada player no ranking, pois a contagem de ranking inicia em 1 (repetição)
                    if i == 1: # Testa se o i é 1 (Isso significa que estamos na primeira repetição do for e o primeiro colocado (player com menor tempo))
                        print("\t\t\t\U0001F947 " + str(i) + "° lugar: " + vencedor +", com "+ str(tempo_minimo_vencedor),"seg ") # Imprime na tela a colocação do jogador a partir do índice i e printa o nome e o tempo minimo do jogador
                        time.sleep(1) 
                    elif i == 2: # Testa se o i é 2 (Isso significa que estamos na segunda repetição do for e o segundo colocado (player com menor tempo))
                        print("\t\t\t\U0001F948 " + str(i) + "° lugar: " + vencedor +", com "+ str(tempo_minimo_vencedor),"seg") # Imprime na tela a colocação do jogador a partir do índice i e printa o nome e o tempo minimo do jogador
                        time.sleep(1)
                    elif i == 3: # Testa se o i é 3 (Isso significa que estamos na terceira repetição do for e o terceiro colocado (player com menor tempo))
                        print("\t\t\t\U0001F949 " + str(i) + "° lugar: " + vencedor +", com "+ str(tempo_minimo_vencedor),"seg") # Imprime na tela a colocação do jogador a partir do índice i e printa o nome e o tempo minimo do jogador
                        time.sleep(1)
                    else: # Se a quantidade de jogadores for maior que três, teremos a execução desse teste com os colocados acima do indice i > 3
                        print("\t\t\t\U0001F494 " + str(i) + "° lugar: " + vencedor +",com "+ str(tempo_minimo_vencedor),"seg") # Imprime na tela a colocação do jogador a partir do índice i e printa o nome e o tempo minimo do jogador
                    del placar[ind_vencedor] # Limpa o valor da lista placar na posição ind_vencedor, pois este já apareceu na tela.
                    del players[ind_vencedor] # Limpa o valor da lista players na posição ind_vencedor, pois este ja apareceu na tela. 
                time.sleep(5) 
                opção_final = input("\nTecle 'v' para voltar ao menu inicial ou 's' para sair \n\u2794\t") # Declaração da variável opção_final para sua validação na condicional. O objetivo é dar um retorno ao usuário e/ou sair do jogo. 
                if opção_final == "s": # Condicional que testa se a opção_final for igual a 's' executará o comando exit().
                    print("Obrigado! Volte logo!")
                    time.sleep(2) 
                    exit() # Sai da execução do jogo      
                elif opção_final == "v": # Condicional que testa se a opção_final for igual a 'v' executará a quebra de laço. 
                    break # Quebra do laço de repetição  'while True:' dos modelos de jogo, o que executa o 'while True:' do Menu. 
            elif modelo_jogo == 2: # Opção que corresponde aos números
                for i in range(0,qtd_jogadores,1): # Estrutua de repeticao responsavel por repetir o processo de jogo () para o numero de participantes
                    print("\n \U0001F6A9 Agora é sua vez ",players[i],", boa sorte! Digite os números que aparecerem o mais rápido que conseguir. \n", sep='')
                    input(" \u26A0 Tecle Enter p/ começar... \u26A0\t")
                    for i in range(3,0,-1):
                        print(i)
                        time.sleep(0.5)  
                    print("Goooo!!\n")         
                    for i in range(0,qtd_sorteios,1):
                        sorteio = random.randint(0,100) # Declara a variável sorteio com o sorteio de números aleatórios entre 0 a 100
                        tempo_antes = time.time() # Declara o tempo_antes de digitar uma variável, com o valor da time.time() 
                        val_numero = int(input("["+ str(sorteio) +"] = "))
                        while val_numero != sorteio:
                            val_numero = int(input("[" + str(sorteio) + "] = "))
                            continue 
                        tempo_depois = time.time() # Declara o tempo_depois com o valor guardado em time.time após digitar uma variável
                        tempo_uma_rodada = tempo_depois - tempo_antes
                        vetor_tempo_rodada.append(tempo_uma_rodada) # vetor_tempo_rodada = lista com todos os tempos_uma_rodada de um player
                        tempo_partida = 0
                    for i in range(len(vetor_tempo_rodada)):
                        tempo_partida = tempo_partida + vetor_tempo_rodada[i]
                    vetor_tempo_rodada.clear()
                    placar.append(round(tempo_partida, 2))
                print("\nE o(a) vencedor(a) foi...  \n")
                time.sleep(2) 
                print("\U0001F914\U0001F914\U0001F914\n") 
                time.sleep(1) 
                print("\t\t\t  >>> \U0001F3C6 >>> RANKING <<< \U0001F3C6 <<<\n")
                for i in range(len(placar)):
                    tempo_minimo_vencedor = min(placar)
                    ind_vencedor = placar.index(tempo_minimo_vencedor)
                    vencedor = players[ind_vencedor]
                    i = i + 1
                    if i == 1:
                        print("\t\t\t\U0001F947 " + str(i) + "° lugar: " + vencedor +", com "+ str(tempo_minimo_vencedor),"seg ")
                        time.sleep(1) 
                    elif i == 2:
                        print("\t\t\t\U0001F948 " + str(i) + "° lugar: " + vencedor +", com "+ str(tempo_minimo_vencedor),"seg")
                        time.sleep(1) 
                    elif i == 3:   
                        print("\t\t\t\U0001F949 " + str(i) + "° lugar: " + vencedor +", com "+ str(tempo_minimo_vencedor),"seg")
                        time.sleep(1) 
                    else:
                        print("\t\t\t\U0001F494 " + str(i) + "° lugar: " + vencedor +",com "+ str(tempo_minimo_vencedor),"seg") 
                    del placar[ind_vencedor]
                    del players[ind_vencedor]
                time.sleep(5) 
                opção_final = input("\nTecle 'v' para voltar ao menu inicial ou 's' para sair \n\u2794\t")
                if opção_final == "s":
                    print("Obrigado! Volte logo!")
                    time.sleep(2)
                    exit()       
                elif opção_final == "v":
                    break
            elif modelo_jogo == 3:
                for i in range(0,qtd_jogadores,1): 
                    print("\n \U0001F6A9 Agora é sua vez ",players[i],", boa sorte! Digite as palavras que aparecerem dentro do [] o mais rápido que conseguir. \n", sep='')
                    input(" \u26A0 Tecle Enter p/ começar... \u26A0\t")  
                    for i in range(3,0,-1):
                        print(i)
                        time.sleep(0.5)  
                    print("Goooo!!")       
                    for i in range(0,qtd_sorteios,1):
                        sorteio = random.choice(lista_palavras) # Sorteia valores de posições aleatórias da lista_palavras. 
                        tempo_antes = time.time() # Declara o tempo_antes de digitar uma variável, com o valor da time.time()  
                        val_palavra = input("["+ sorteio +"] = ")
                        while val_palavra != sorteio:
                            val_palavra = input("[" + sorteio + "] = ")
                            continue 
                        tempo_depois = time.time() # Declara o tempo_depois com o valor guardado em time.time após digitar uma variável
                        tempo_uma_rodada = tempo_depois - tempo_antes 
                        vetor_tempo_rodada.append(tempo_uma_rodada)
                        tempo_partida = 0
                    for i in range(len(vetor_tempo_rodada)):
                        tempo_partida = tempo_partida + vetor_tempo_rodada[i]
                    vetor_tempo_rodada.clear()
                    placar.append(round(tempo_partida, 2))
                print("\nE o(a) vencedor(a) foi...  \n")
                time.sleep(2) 
                print("\U0001F914\U0001F914\U0001F914\n") 
                time.sleep(1) 
                print("\t\t\t  >>> \U0001F3C6 >>> RANKING <<< \U0001F3C6 <<<\n")
                for i in range(len(placar)):
                    tempo_minimo_vencedor = min(placar)
                    ind_vencedor = placar.index(tempo_minimo_vencedor)
                    vencedor = players[ind_vencedor]
                    i = i + 1
                    if i == 1:
                        print("\t\t\t\U0001F947 " + str(i) + "° lugar: " + vencedor +", com "+ str(tempo_minimo_vencedor),"seg ")
                        time.sleep(1) 
                    elif i == 2:
                        print("\t\t\t\U0001F948 " + str(i) + "° lugar: " + vencedor +", com "+ str(tempo_minimo_vencedor),"seg")
                        time.sleep(1) 
                    elif i == 3:   
                        print("\t\t\t\U0001F949 " + str(i) + "° lugar: " + vencedor +", com "+ str(tempo_minimo_vencedor),"seg")
                        time.sleep(1)
                    else:
                        print("\t\t\t\U0001F494 " + str(i) + "° lugar: " + vencedor +",com "+ str(tempo_minimo_vencedor),"seg")
                    del placar[ind_vencedor]
                    del players[ind_vencedor]
                time.sleep(5)  
                opção_final = input("\nTecle 'v' para voltar ao menu inicial ou 's' para sair  \n\u2794 " )
                if opção_final == "s":
                    print("Obrigado! Volte logo!")
                    time.sleep(2) 
                    exit()       
                elif opção_final == "v":
                    break
            elif modelo_jogo == 4: 
                for i in range(0,qtd_jogadores,1): 
                    print("\n \U0001F6A9 Agora é sua vez ",players[i],", boa sorte! Digite as sentenças que aparecerem o mais rápido que conseguir. \n", sep='')
                    input(" \u26A0 Tecle Enter p/ começar... \u26A0\t")  
                    for i in range(3,0,-1):
                        print(i)
                        time.sleep(0.5) 
                    print("Goooo!!")       
                    for i in range(0,qtd_sorteios,1):
                        sorteio = random.choice(lista_sentenças) # Sorteia valores em posições aleatórias da lista_sentenças
                        tempo_antes = time.time() # Declara o tempo_antes de digitar uma variável, com o valor da time.time()  
                        val_sentença = input("["+ sorteio +"] = ")
                        while val_sentença != sorteio:
                            val_sentença = input("[" + sorteio + "] = ")
                            continue 
                        tempo_depois = time.time() # Declara o tempo_depois com o valor guardado em time.time após digitar uma variável
                        tempo_uma_rodada = tempo_depois - tempo_antes 
                        vetor_tempo_rodada.append(tempo_uma_rodada)
                        tempo_partida = 0
                    for i in range(len(vetor_tempo_rodada)):
                        tempo_partida = tempo_partida + vetor_tempo_rodada[i]
                    vetor_tempo_rodada.clear()
                    placar.append(round(tempo_partida, 2))
                print("\nE o(a) vencedor(a) foi...  \n")
                time.sleep(2) 
                print("\U0001F914\U0001F914\U0001F914\n") 
                time.sleep(1) 
                print("\t\t\t  >>> \U0001F3C6 >>> RANKING <<< \U0001F3C6 <<<\n")
                for i in range(len(placar)):
                    tempo_minimo_vencedor = min(placar)
                    ind_vencedor = placar.index(tempo_minimo_vencedor)
                    vencedor = players[ind_vencedor]
                    i = i + 1
                    if i == 1:
                        print("\t\t\t\U0001F947 " + str(i) + "° lugar: " + vencedor +", com "+ str(tempo_minimo_vencedor),"seg ")
                        time.sleep(1) 
                    elif i == 2:
                        print("\t\t\t\U0001F948 " + str(i) + "° lugar: " + vencedor +", com "+ str(tempo_minimo_vencedor),"seg")
                        time.sleep(1) 
                    elif i == 3:   
                        print("\t\t\t\U0001F949 " + str(i) + "° lugar: " + vencedor +", com "+ str(tempo_minimo_vencedor),"seg")
                        time.sleep(1) 
                    else:
                        print("\t\t\t\U0001F494 " + str(i) + "° lugar: " + vencedor +",com "+ str(tempo_minimo_vencedor),"seg") 
                    del placar[ind_vencedor]
                    del players[ind_vencedor]
                time.sleep(5) 
                opção_final = input("\nTecle 'v' para voltar ao menu inicial ou 's' para sair \n\u2794\t")
                if opção_final == "s":
                    print("Obrigado! Volte logo!")
                    time.sleep(2) 
                    exit()       
                elif opção_final == "v":
                    break
            break
    elif opção == 2:        # 2° OPÇÃO DO MENU
        
        print("""
    \t\t\t    >>> MENU DE CONFIGURAÇÕES <<<

    1 \u2794  \U0001F574 Quantidade de jogadores por partida:""", qtd_jogadores ,"""
    2 \u2794  \U0001F3B2 Quantidade de sorteios por partida, quantidade atual:""", qtd_sorteios ,"""
    3 \u2794  \u274C Sair

Qual das configurações você gostaria de alterar? (1 ou 2 para opções, 3 para sair) """)
        opção_config = int(input("\u2794  ")) 
        print("\u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699 \u2699  \n")
        while True: #Laço de repetição para testar e executar as opções do menu
            if opção_config == 1: # Quantidade de jogadores por partida
                print("\t   >>> \U0001F574 Digite a quantidade de jogadores por partida (2 a 5) \U0001F574 <<<")
                qtd_jogadores = int(input("\u2794  "))
                while not (2 <= qtd_jogadores <= 5): # Laço de repetição para insistir até a resposta esperada
                    print("Quantidade inválida! Digite o número de players de 2 a 5")
                    qtd_jogadores = int(input("\u2794  "))
                    break
                break
            elif opção_config == 2: # Quantidade de sorteios por partida, quantidade atual
                print("\t  >>> \U0001F3B2 Digite a quantidade de sorteios por partida (5 a 10) \U0001F3B2 <<<")
                qtd_sorteios = int(input("\u2794  "))
                while not (5 <= qtd_sorteios <= 10):
                    print("Quantidade inválida! Digite o número de sorteios de 5 a 10")
                    qtd_sorteios = int(input("\u2794  "))
                    break
                break
            else: 
                print("Opção inválida! Tente novamente! \U0001F481 \U0001F64E")
                break
    elif opção == 3:
        print("\t\t\t\t    \U0001F4DC Sobre o Jogo \U0001F4DC\n")
        time.sleep(1) 
        print("História do Jogo: A história do Flash Cata Milho se inicía após o nascimento do garotinho Barry Allen. Ele nasceu no ínicio do século 20, época em que as máquinas de escrever eram uma febre, assim como os datilográfos. O pai de Barry era um datilógrafo famoso, sempre ensinava ao seu filho as técnicas de digitação desde cedo. Mas Barry sempre demorava um tempo maior para digitar que seus colegas.",end=' ')
        time.sleep(23) 
        print("\U0001F516 Certa vez em um campeonato de datilografia que ocorreu na escola, o tempo de digitação do Allen foi tão grande que ele foi desclassificado do campeonato. Esse dia foi traumatizante para Barry, pois ele se via incapaz de seguir o legado de seu pai. Triste e desmotivado, Barry decide sair do ginásio onde ocorria o campeonato. Era um dia de forte tempestade, chovia muito, muitos raios e trovoadas. Mas o Barry só queria estar em seu quarto, pois lá ninguém poderia rir da cara dele, então ele correu dali.",end=' ') 
        time.sleep(25) 
        print("\U0001F516 Em meio a fortes chuvas, Barry corria! Corria, corria e corria. Em sua cabeça só passava o questionamento, 'por que aquele monte de cata milho digitam mais rápido do que eu?'. Chegando a poucos metros de sua casa, caiu um raio do céu que atingiu Barry. Quando foi atingido pelo raio, Allen desmaiou, em seguida foi levado para o médico ainda com vida. Ficou em coma por 6 meses, e então voltou a ter saúde.",end='') 
        time.sleep(29) 
        print("\U0001F516 Certo dia vendo seu pai cansado na sala digitando um livro, ofereceu ajuda ao seu pai. Barry perguntou 'Pai! Posso ajudar o senhor a catar milhos?' o pai dele surpreso e desconfiante cedeu a cadeira para o filho. Para surpresa do pai e do próprio Barry ele digitou uma folha 100.000 vezes mais rápido que o pai. A ampulheta do pai de Barry só tinha derramado 1 grão de areia, e toda redação estava escrita. Ambos ficaram muito felizes, e foi questão de dias até toda cidade saber.",end=' ')
        time.sleep(32) 
        print("\U0001F516 Todos os moradores da cidade ficavam curiosos com a história de Barry e queriam desafiá-lo amistosamente. Ele era chamado pela mídia como 'O Flash Catador de Milhos'. Para orquestrar tal campeonato, a equipe da escola contratou três programadores (Fabricia E., Lucas A. e Yago) para fazer um programa que sorteasse letras, numeros, sentenças ou palavras. Tal programa, iria marcar o tempo inicial e final da digitação. Quem digitasse mais rápido venceria o Flash. Os próximos cápitulos dessa história é você quem escreve, jogando nosso querido jogo. O Flash Cata Milhos, será o vencedor da partida.")    
        time.sleep(34) 
        print("\n              \t\t\t \U0001F3AE \u24BF \u24C4 \u24BC \u24C4 \U0001F3AE \n")
        time.sleep(1) 
        print("\U0001F3AF Objetivo do jogo: Testar a velorcidade da digitação dos players.\n") 
        time.sleep(2.2)
        print("\U0001F47D São permitidos no máximo 5 players por partida.\n")  
        time.sleep(3)        
        print("""\U0001F3B2 Fica a critério dos players a escolha da variável a ser sorteada, você pode optar por:
* Letras \u2794  Vão ser sorteadas letras do alfabeto brasileiro de A-Z.
* Números \u2794  Números inteiros (0 - 100).
* Palavras \u2794  Palavras engraçadas e aleatórias.
* Sentenças \u2794  Sentenças aleatórias que enrolam a língua.\n""")
        time.sleep(13) 
        print("""\U0001F3AE Dicas de jogabilidade: 
\u267E Digite o mais rápido que conseguir.
\u267E No caso de digitacao incorreta, sera solicitado o input novamente, e o tempo total sera contabilizado.
\u267E Posicione as mão frente ao teclado de forma ergonômica.
\u267E Vença seus oponentes digitando rapido como o Flash! \u231B\n
\U0001F5AE Teclas: 
\u21B5 A tecla enter valida suas opções e envia sua digitação no jogo\n""")
        time.sleep(13) 
        print("\t\tDesenvolvido e Editado por Fabricia E., Lucas N., Yago M. (2022)")
        input("\t\t\t \u2B8C Tecle enter para voltar ao menu inicial \u2B8C  ")
    elif opção == 4:            # 3° OPÇÃO DO MENU 
        print("Obrigado! Volte logo! \U0001F64B")
        break # Quebra o laço de repetição do MENU
    else: # Se a opção digitada no MENU for fora do intervalo 1 a 4 
        print("Opção Inválida")
        