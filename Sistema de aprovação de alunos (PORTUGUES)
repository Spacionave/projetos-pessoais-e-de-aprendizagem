# Lista para armazenar os nomes dos alunos
aluno = []

# Lista para armazenar as notas (cada aluno terá uma lista com 3 notas)
notas = []


# Função para cadastrar um novo aluno
def CadastrarAluno():
    # Pede o nome do aluno
    nome = input("Digite o nome do aluno: ")
    
    # Pede as 3 notas do aluno
    n1 = float(input("Digite a 1° nota: "))
    n2 = float(input("Digite a 2° nota: "))
    n3 = float(input("Digite a 3° nota: "))

    # Adiciona o nome na lista de alunos
    aluno.append(nome)
    
    # Adiciona as notas em forma de lista dentro da lista "notas"
    notas.append([n1, n2, n3])


# Função para listar todos os alunos cadastrados
def ListarAlunos():
    # Verifica se não há alunos cadastrados
    if len(aluno) == 0:
        print("Não há alunos cadastrados")
    else:
        # Percorre a lista de alunos
        for i in range(len(aluno)):
            # Mostra o índice + nome + notas do aluno
            print(f"{i+1} - {aluno[i]} -  notas: {notas[i]}")


# Função para remover um aluno
def RemoverAluno():
    # Verifica se há alunos
    if len(aluno) == 0:
        print("Não há alunos cadastrados")
    else:
        # Mostra a lista de alunos
        ListarAlunos()
        
        # Pede o número do aluno que deseja remover
        indice = int(input("Digite o aluno que deseja remover: ")) - 1
        
        # Verifica se o índice é válido
        if 0 <= indice < len(aluno):
            # Remove o aluno e suas notas
            aluno.pop(indice)
            notas.pop(indice)
            print("Aluno removido com sucesso!")


# Função para calcular e mostrar a média de cada aluno
def VerMedia():
    # Verifica se há alunos cadastrados
    if len(aluno) == 0:
        print("Não há alunos cadastrados")
    else:
        # Percorre todos os alunos
        for i in range(len(aluno)):
            # Calcula a média das 3 notas
            media = sum(notas[i]) / 3
            
            # Mostra o nome do aluno e sua média
            print(f"{aluno[i]} - média: {media:.2f}")


# Função para mostrar a qualificação do aluno com base na média
def VerQualifica():
    # Verifica se há alunos cadastrados
    if len(aluno) == 0:
        print("Não há alunos cadastrados")
    else:
        # Percorre todos os alunos
        for i in range(len(aluno)):
            # Calcula a média
            media = sum(notas[i]) / 3

            # Verifica a classificação do aluno
            if media >= 8:
                print(f"{aluno[i]} - EXCELENTE")
            elif media >= 6:
                print(f"{aluno[i]} - BOM")
            elif media >= 5:
                print(f"{aluno[i]} - REGULAR")
            else:
                print(f"{aluno[i]} - REPROVADO")


# Loop principal do programa (menu)
while True:
    print("\n===========MENU=============")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Remover alunos")
    print("4 - Ver media do aluno")
    print("5 - Ver qualificação do aluno")
    print("6 - Sair")

    # Pede a opção do usuário
    opcao = input("Digite sua opção: ")

    # Verifica qual opção foi escolhida e chama a função correspondente
    if opcao == "1":
        CadastrarAluno()
    elif opcao == "2":
        ListarAlunos()
    elif opcao == "3":
        RemoverAluno()
    elif opcao == "4":
        VerMedia()
    elif opcao == "5":
        VerQualifica()
    elif opcao == "6":
        print("Fim do programa")
        break  # Encerra o programa
