import json
import os

ARQUIVO = "registros.json"

def carregar_registros():
    global proximo_id
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            dados = json.load(f)
            proximo_id = dados["proximo_id"]
            return dados["registros"]
    else:
        proximo_id = 1
        return []
def salvar_registros():
    with open(ARQUIVO, "w") as f:
        json.dump({"proximo_id": proximo_id, "registros": registros}, f, indent=4)

registros = carregar_registros()

def incluir_registro():
    global proximo_id

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    registro = {
        "id" : proximo_id,
        "nome" : nome,
        "idade" : idade
    }
    registros.append(registro)
    print(f" Registro {proximo_id} incluido com sucesso!!")

    proximo_id += 1
    salvar_registros()

def buscar_registro():
    id_busca = int(input("Digite o id para busca:"))
    for registro in registros:
        if registro["id"] == id_busca:
            print(f"\n ID: {registro['id']}, Nome: {registro['nome']}, Idade: {registro['idade']}")
            return
    print("Registro não encontrado!")

def excluir_registro():
    id_exclusao = int(input("Digite o id à ser exluido: "))
    for registro in registros:
        if registro["id"] == id_exclusao:
            registros.remove(registro)
            salvar_registros()
            print("Registro excluido com sucesso!")
            return
    print("Registro não encontrado")
while True:
    print("\n=== MENU ===")
    print("1. Incluir registro")
    print("2. Buscar registro")
    print("3. Excluir registro")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        incluir_registro()
    elif opcao == "2":
        buscar_registro()
    elif opcao == "3":
        excluir_registro()
    elif opcao == "4":
        print("Encerrando programa...")
        break
    else:
        print("Opção invalida, tente novamente")


