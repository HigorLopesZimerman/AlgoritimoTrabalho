dados = [
    {"codigo": 8, "nome": "José", "endereco": "Rua F, 90", "cidade": "Cândido Mota", "uf": "SP"},
    {"codigo": 14, "nome": "Carina", "endereco": "Rua F, 25", "cidade": "Assis", "uf": "SP"},
    {"codigo": 2, "nome": "Maria", "endereco": "Rua K, 67", "cidade": "Marilia", "uf": "SP"},
    {"codigo": 11, "nome": "Silvia", "endereco": "Rua B, 203", "cidade": "Assis", "uf": "SP"},
    {"codigo": 6, "nome": "Pedro", "endereco": "Rua J, 38", "cidade": "Assis", "uf": "SP"},
]



indices = [
    (2, 2),
    (6, 4),
    (8, 0),
    (11, 3),
    (14, 1)
]


def Buscar_arquivo():
    busca = int(input("\nInsira o id do arquivo desejado: "))
    for cod, pos in indices:
        if cod == busca:
            print(f"Id encontrado:\n")
            registro = dados[pos]
            for chave, valor in registro.items():
                print(f"{chave} : {valor}")

       
            return None
    print("\nId não encontrado")

def menu():
    while True:
        print("\n=== MENU ARQUIVO INDEXADOS")
        print("1 - Buscar arquivos")
        print("0 - Sair")

        option = int(input("Escolha uma opção: "))

        if option == 1:
            Buscar_arquivo()
        elif option == 0:
            print("Saindo...")
            break
        else:
            print("Opção invalida")

menu()
