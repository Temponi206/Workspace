jogador1="x"
jogador2="o"
tabuleiro=[[1,2,3],[4,5,6],[7,8,9]]
def jogar():
    ultimo_a_jogar=""
    mostrar_tabuleiro()
    while True:
        if ultimo_a_jogar=="Jogador 2" or ultimo_a_jogar=="":
            try:
                jogada=int(input(f"Jogador 1 escolha um numero: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                continue
            if jogada<1 or jogada>9:
                print("Número inválido. Por favor, escolha um número entre 1 e 9.")
                mostrar_tabuleiro()
                continue
            ultimo_a_jogar="Jogador 1"
        else:    
            try:
                jogada=int(input(f"Jogador 2 escolha um numero: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                continue
            if jogada<1 or jogada>9:
                print("Número inválido. Por favor, escolha um número entre 1 e 9.")
                mostrar_tabuleiro()
                continue
            ultimo_a_jogar="Jogador 2"
        for i in range(0,3):
            for j in range(0,3):
                if tabuleiro[i][j]==jogada:
                    tabuleiro[i][j]=jogador1 if ultimo_a_jogar=="Jogador 1" else jogador2
        if verificar_vitoria():
            mostrar_tabuleiro()
            if ultimo_a_jogar=="Jogador 1":
                print(f"Jogador 1 venceu!")
                exit()
            else:
                print(f"Jogador 2 venceu!")
                exit()
        if tabuleiro_cheio(tabuleiro):
            mostrar_tabuleiro()
            print("Empate!")
            exit()
        
        mostrar_tabuleiro()
def mostrar_tabuleiro():
    for i in range(0,3):
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")
def verificar_vitoria():
    for i in range(0,3):
        if tabuleiro[i][0]==tabuleiro[i][1]==tabuleiro[i][2]:
            return True
        if tabuleiro[0][i]==tabuleiro[1][i]==tabuleiro[2][i]:
            return True
    if tabuleiro[0][0]==tabuleiro[1][1]==tabuleiro[2][2]:
        return True
    if tabuleiro[0][2]==tabuleiro[1][1]==tabuleiro[2][0]:
        return True
    return False
def tabuleiro_cheio(tabuleiro):
    for linha in tabuleiro:
        for valor in linha:
            if isinstance(valor, int):
                return False
    return True
jogar()