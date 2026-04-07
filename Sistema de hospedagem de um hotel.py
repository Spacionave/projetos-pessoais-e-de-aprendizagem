# ===============================================
# SISTEMA DE RESERVAS - HOTEL SANTO AMARO
# Feito por: Leonardo Lima
# ===============================================

# Valor fixo da diária
valor_diaria = 120

# Lista que guarda todas as reservas
reservas = []

# Quantos quartos o hotel tem disponíveis
quartos_disponiveis = 5


# -------- FUNÇÃO PARA FAZER UMA RESERVA --------
def fazer_reserva(quartos_disponiveis, reservas):
    # Se não tiver mais quartos
    if quartos_disponiveis == 0:
        print("Não há mais quartos disponíveis.")
        return quartos_disponiveis, reservas  # retorna os mesmos valores sem mudar nada

    # Pede os dados do hóspede
    nome = input("Digite o nome do hóspede: ")
    dias = int(input("Quantos dias ele vai ficar? "))

    # Calcula o valor total
    valor_total = dias * valor_diaria

    # Cria a reserva e adiciona na lista
    reserva = {"nome": nome, "dias": dias, "valor": valor_total}
    reservas.append(reserva)

    # Diminui 1 quarto disponível
    quartos_disponiveis -= 1

    print(f"\nReserva feita com sucesso para {nome}!")
    print(f"Valor total: R${valor_total:.2f}")
    print(f"Quartos restantes: {quartos_disponiveis}")

    return quartos_disponiveis, reservas  # devolve os valores atualizados


# -------- FUNÇÃO PARA MOSTRAR OS HÓSPEDES --------
def listar_hospedes(reservas):
    if len(reservas) == 0:
        print("Nenhum hóspede cadastrado ainda.")
    else:
        print("\nLista de hóspedes:")
        for i, reserva in enumerate(reservas, start=1):
            print(f"{i}. Nome: {reserva['nome']} | Dias: {reserva['dias']} | Valor: R${reserva['valor']:.2f}")


# -------- FUNÇÃO PARA MOSTRAR O TOTAL DE DINHEIRO --------
def mostrar_relatorio(reservas):
    total = 0
    for reserva in reservas:
        total += reserva["valor"]

    print(f"\nO total arrecadado até agora é: R${total:.2f}")


# -------- MENU PRINCIPAL --------
def menu():
    quartos_disponiveis = 5
    reservas = []

    while True:
        print("\n========= MENU PRINCIPAL =========")
        print("1 - Fazer reserva")
        print("2 - Listar hóspedes")
        print("3 - Mostrar relatório financeiro")
        print("4 - Sair do sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            quartos_disponiveis, reservas = fazer_reserva(quartos_disponiveis, reservas)
        elif opcao == "2":
            listar_hospedes(reservas)
        elif opcao == "3":
            mostrar_relatorio(reservas)
        elif opcao == "4":
            print("\nSaindo do sistema... Obrigado por usar o Hotel Santo Amaro!")
            break
        else:
            print("Opção inválida! Tente novamente.")


# -------- INÍCIO DO PROGRAMA --------
menu()
