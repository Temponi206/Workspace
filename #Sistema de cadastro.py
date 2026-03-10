from random import *
#Sistema de cadastro da netflix
saldo=0
clientes=[]
cpf=""
basico=0
medio=0
completo=0
primeiros_nomes = [
    "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Henrique", "Isabela", "João",
    "Kamila", "Lucas", "Mariana", "Nicolas", "Olívia", "Pedro", "Queila", "Rafael", "Sofia", "Thiago",
    "Ursula", "Vinícius", "Wesley", "Xênia", "Yasmin", "Zeca", "Amanda", "Beatriz", "Caio", "Diego",
    "Elaine", "Fernanda", "Gustavo", "Helena", "Igor", "Juliana", "Karen", "Leonardo", "Melissa", "Natália",
    "Otávio", "Paula", "Renato", "Samuel", "Talita", "Valentina", "William", "Bianca", "Cecília", "Murilo"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
plan=["basico","medio","completo"]
planos={"basico":22,"medio":40,"completo":60}
for i in range (0,100):
    cpf=""
    cliente=[]
    nome=choice(primeiros_nomes)
    idade=randint(16,99)
    #criando o cpf aleatoriamente
    for i in range(0,3):
        for j in range(0,3):
            cpf+=choice(numeros)
        if len(cpf)<9:
            cpf+="."
        else:
            cpf+="-"
    for i in range(0,2):
        cpf+=choice(numeros)
    
    plano=choice(plan)
    meses=randint(1,36)
    valor_final=planos.get(plano)*meses
    saldo+=valor_final
    cliente+=[nome,idade,cpf,plano]
    clientes.append(cliente)

    print(f"Cliente: {nome} - Idade: {idade} - CPF: {cpf} - Plano: {plano}")
for i in [cliente[3] for cliente in clientes]:
    if i=="basico":
        basico+=1
    elif i=="medio":
        medio+=1
    else:
        completo+=1

print(f"Voce conseguiu {saldo} ate parar de cadastrar")
print(f"Seu banco de dados contem {len(clientes)}")
print(f"media de idade dos clientes: {sum([cliente[1] for cliente in clientes])/len(clientes)}")
print(f"Clientes no plano básico: {basico}")
print(f"Clientes no plano médio: {medio}")
print(f"Clientes no plano completo: {completo}")
