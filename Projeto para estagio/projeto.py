# Sistema de Recomendação de Produtos

# Estruturas dos dados
produtos = {}
usuarios = {}

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto: ")
    preco = float(input("Digite o preço do produto: "))
    
    # Aqui é feita a verificação se o produto já existe ou não
    if (nome, categoria) not in produtos:
        produtos[(nome, categoria)] = preco
        print("Produto cadastrado com sucesso!")
    else:
        print("Produto já cadastrado na mesma categoria.")

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    
    # Aqui é feita a verificação se o usuário já existe
    if nome not in usuarios:
        usuarios[nome] = {"favoritos": []}
        print("Usuário adicionado com sucesso!")
    else:
        print("Usuário já existe.")

def adicionar_favorito():
    nome_usuario = input("Digite o nome do usuário: ")
    if nome_usuario in usuarios:
        produto_nome = input("Digite o nome do produto: ")
        produto_categoria = input("Digite a categoria do produto: ")
        
        # Verificando se o produto existe
        if (produto_nome, produto_categoria) in produtos:
            favorito = (produto_nome, produto_categoria)
            if favorito not in usuarios[nome_usuario]["favoritos"]:
                usuarios[nome_usuario]["favoritos"].append(favorito)
                print("Produto adicionado aos favoritos.")
            else:
                print("Produto já está nos favoritos.")
        else:
            print("Produto não encontrado.")
    else:
        print("Usuário não encontrado.")

def ver_recomendacoes():
    nome_usuario = input("Digite o nome do usuário: ")
    if nome_usuario in usuarios:
        categorias_favoritas = set(produto[1] for produto in usuarios[nome_usuario]["favoritos"])
        print(f"Recomendações para {nome_usuario}:")
        for (nome, categoria), preco in produtos.items():
            if categoria in categorias_favoritas and (nome, categoria) not in usuarios[nome_usuario]["favoritos"]:
                print(f"- {nome} ({categoria}) - R$ {preco:.2f}")
    else:
        print("Usuário não encontrado.")

def menu():
    while True:
        print("\nBem vindo ao Sistema de recomendações BCB!")
        print("1. Cadastrar Produto")
        print("2. Cadastrar Usuário")
        print("3. Adicionar Produto aos Favoritos")
        print("4. Ver recomendações")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cadastrar_produto()
        elif escolha == '2':
            cadastrar_usuario()
        elif escolha == '3':
            adicionar_favorito()
        elif escolha == '4':
            ver_recomendacoes()
        elif escolha == '5':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida! Tente novamente.")

# execucão do  menu
menu()

