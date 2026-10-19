# Desafio - Controle de ingressos do evento escolar

def verificar_evento():
    print("=== Controle de Ingressos - Evento Escolar ===")
    print("Temos 100 ingressos no total e no máximo 20 convidados\n")

    try:
        alunos = int(input("Quantidade de alunos: "))
        monitores = int(input("Quantidade de monitores: "))
        convidados = int(input("Quantidade de convidados: "))
    except ValueError:
        print("Por favor, digite apenas números inteiros!")
        return

    total_pessoas = alunos + monitores + convidados
    ingressos_disponiveis = 100
    limite_convidados = 20

    print(f"\nTotal de pessoas: {total_pessoas}")
    print(f"Total de convidados: {convidados}\n")

    # Verificação das regras
    if total_pessoas > ingressos_disponiveis and convidados > limite_convidados:
        print(f"❌ Não será possível realizar o evento!")
        print(f"Motivo 1: Você ultrapassou o total de ingressos em {total_pessoas - ingressos_disponiveis} pessoas.")
        print(f"Motivo 2: Você ultrapassou o limite de convidados. Máximo permitido é {limite_convidados}.")
    
    elif total_pessoas > ingressos_disponiveis:
        print(f"❌ Limite de ingressos excedido!")
        print(f"Você precisa de {total_pessoas} ingressos, mas só temos {ingressos_disponiveis}.")
        print(f"Reduza {total_pessoas - ingressos_disponiveis} pessoas.")

    elif convidados > limite_convidados:
        print(f"❌ Limite de convidados excedido!")
        print(f"Você informou {convidados} convidados, mas o limite é de {limite_convidados}.")
        print(f"Mesmo que o total de ingressos ({total_pessoas}/100) esteja ok, a direção não permite mais de 20 convidados.")

    else:
        vagas_restantes = ingressos_disponiveis - total_pessoas
        print(f"✅ Evento liberado! Tudo dentro das regras.")
        print(f"Ingressos usados: {total_pessoas}/100")
        print(f"Vagas restantes: {vagas_restantes}")

# Executa o programa
verificar_evento()
