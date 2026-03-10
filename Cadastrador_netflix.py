from random import *
def gerar_cpf():
    cpf=""
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(0,3):
        for j in range(0,3):
            cpf+=choice(numeros)
        if len(cpf)<9:
            cpf+="."
        else:
            cpf+="-"
    for i in range(0,2):
        cpf+=choice(numeros)
    return cpf
def listar_clientes(clientes):
    for cliente in clientes:
        print(f"Nome: {cliente['nome']}, Idade: {cliente['idade']}, CPF: {cliente['cpf']}, Plano: {cliente['plano']}, Meses contratados: {cliente['meses']}, Valor pago: R${cliente['valor_pago']}")
def buscar_por_nome():
    nome_busca = input("Digite o nome que deseja buscar: ").lower()

    encontrou = False

    for cliente in clientes:
        if cliente["nome"].lower() == nome_busca:
            print(f"Nome: {cliente['nome']} | CPF: {cliente['cpf']} | Plano: {cliente['plano']} | Meses contratados: {cliente['meses']} | Valor pago: R${cliente['valor_pago']}")
            encontrou = True

    if not encontrou:
        print("Cliente não encontrado.")
#Sistema de cadastro da netflix
basico = 0
medio = 0
completo = 0
faturamento_total=0
clientes=[]
primeiros_nomes = [
    "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Henrique", "Isabela", "João",
    "Kamila", "Lucas", "Mariana", "Nicolas", "Olívia", "Pedro", "Queila", "Rafael", "Sofia", "Thiago",
    "Ursula", "Vinícius", "Wesley", "Xênia", "Yasmin", "Zeca", "Amanda", "Beatriz", "Caio", "Diego",
    "Elaine", "Fernanda", "Gustavo", "Helena", "Igor", "Juliana", "Karen", "Leonardo", "Melissa", "Natália",
    "Otávio", "Paula", "Renato", "Samuel", "Talita", "Valentina", "William", "Bianca", "Cecília", "Murilo"]

planos={"basico":22,"medio":40,"completo":60}

for _ in range (0,repeticoes:=int(input("Digite a quantidade de clientes a serem cadastrados: "))):
    cliente={}
    cliente["nome"] = choice(primeiros_nomes)
    cliente["idade"]=randint(16,99)
    cliente["cpf"]=gerar_cpf() 
    cliente["plano"]=choice(list(planos.keys()))
    cliente["meses"]=randint(1,36)
    cliente["valor_pago"]=planos.get(cliente["plano"])*cliente["meses"]
    faturamento_total+=cliente["valor_pago"]
    clientes.append(cliente)

    if cliente["plano"] == "basico":
        basico += 1
    elif cliente["plano"] == "medio":
        medio += 1
    elif cliente["plano"] == "completo":
        completo += 1
print(f"Faturamento total: R$ {faturamento_total}")
print(f"Quantidade de clientes: {len(clientes)}")
print(f"Media de meses contratados: {faturamento_total/sum(cliente['meses'] for cliente in clientes):.2f}")
print(f"O plano basico faturou R$ {100planos['basico']*sum(cliente['meses'] for cliente in clientes if cliente['plano'] == 'basico'):.2f}")
print(f"O plano medio faturou R$ {planos['medio']*sum(cliente['meses'] for cliente in clientes if cliente['plano'] == 'medio'):.2f}")
print(f"O plano completo faturou R$ {planos['completo']*sum(cliente['meses'] for cliente in clientes if cliente['plano'] == 'completo'):.2f}")
if basico > medio and basico > completo:
    print("Plano mais vendido: básico")
elif medio > basico and medio > completo:
    print("Plano mais vendido: médio")
elif completo > basico and completo > medio:
    print("Plano mais vendido: completo")
else:
    print("Houve empate entre os planos mais vendidos")
if input("Deseja listar os clientes? (s/n) ")=="s":
    listar_clientes(clientes)
if input("Deseja buscar um cliente por nome? (s/n) ")=="s":
    buscar_por_nome()
    print("Busca finalizada.")

