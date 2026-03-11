from random import *
control=0
tentativas=0
maximo=int(input("Digite o numero maximo para o jogo: "))
numero = randint(1,maximo)
palpite=int(input("Digite seu palpite: "))

while palpite!=numero:
    control+=1
    if maximo >= 1:
        print("Digite um número maior que zero.")
        break   
    except ValueError:
        print("Digite um número inteiro válido.")
    if palpite>maximo:
        print("palpite invalido, tente novamente")
    
    elif palpite<numero:
        tentativas+=1
        print("O numero é maior")
    
    else:
        tentativas+=1
        print("O numero é menor")
    if tentativas==5:
        print("Dica: O numero é par" if numero%2==0 else "Dica: O numero é impar")
    if control%5==0:
        if input("Deseja desistir? (s/n) ")=="s":
            print(f"O numero era {numero}")
            exit()
    palpite=int(input("Digite seu palpite: "))

tentativas+=1
print(f"Parabens voce acertou o numero em {tentativas} tentativas")
