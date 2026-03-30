aluno = []
notas = []

def CadastrarAluno():
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a 1° nota: "))
    n2 = float(input("Digite a 2° nota: "))
    n3 = float(input("Digite a 3° nota: "))

    aluno.append(nome)
    notas.append([n1, n2, n3])

def ListarAlunos():
    if len(aluno) == 0:
        print("Não há alunos cadastrados")
    else:
        for i in range(len(aluno)):
            print(f"{i+1} - {aluno[i]} -  notas: {notas[i]}")

def RemoverAluno():
    if len(aluno) == 0:
        print("Não há alunos cadastrados")
    else:
        ListarAlunos()
        indice = int(input("Digite o aluno que deseja remover: ")) - 1
        if 0 <= indice < len(aluno):
            aluno.pop(indice)
            notas.pop(indice)
            print("Aluno removido com sucesso!")

def VerMedia():
    if len(aluno) == 0:
        print("Não há alunos cadastrados")
    else:
        for i in range(len(aluno)):
            media = sum(notas[i]) / 3
            print(f"{aluno[i]} - média: {media:.2f}")

def VerQualifica():
    if len(aluno) == 0:
        print("Não há alunos cadastrados")
    else:
        for i in range(len(aluno)):
            media = sum(notas[i]) / 3

            if media >= 8:
                print(f"{aluno[i]} - EXCELENTE")
            elif media >= 6:
                print(f"{aluno[i]} - BOM")
            elif media >= 5:
                print(f"{aluno[i]} - REGULAR")
            else:
                print(f"{aluno[i]} - REPROVADO")

while True:
    print("\n===========MENU=============")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Remover alunos")
    print("4 - Ver media do aluno")
    print("5 - Ver qualificação do aluno")
    print("6 - Sair")

    opcao = input("Digite sua opção: ")

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
        break