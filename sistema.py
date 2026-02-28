import time
import random
import json

# ===== CORES =====
RESET = "\033[m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
CIANO = "\033[36m"
NEGRITO = "\033[1m"

alunos = []


# ===== JSON =====
def salvar():
    with open("alunos.json", "w") as arquivo:
        json.dump(alunos, arquivo)


def carregar():
    global alunos
    try:
        with open("alunos.json", "r") as arquivo:
            alunos = json.load(arquivo)
    except FileNotFoundError:
        alunos = []


# ===== MENU =====
def menu():
    time.sleep(0.3)
    print()
    print(CIANO + NEGRITO + "=== MENU PRINCIPAL ===" + RESET)
    print()
    print(AMARELO + "1 - Ver nota dos alunos" + RESET)
    print(AMARELO + "2 - Alterar alguma nota" + RESET)
    print(AMARELO + "3 - Remover algum aluno" + RESET)
    print(AMARELO + "4 - Adicionar um aluno" + RESET)
    print()
    print(VERMELHO + "0 - Fechar programa" + RESET)
    print()


def cadastrar():
    while True:
        aluno = input("Digite o nome do aluno: ").lower()
        if aluno != "parar":
            dic = {aluno: random.randint(0, 10)}
            alunos.append(dic)
            salvar()
        else:
            break


def turma():
    print()
    print(AZUL + NEGRITO + "=== LISTA DE ALUNOS ===" + RESET)
    print()
    if not alunos:
        print(VERMELHO + "Nenhum aluno cadastrado." + RESET)
    for a, n in enumerate(alunos, start=1):
        for nome, nota in n.items():
            print(CIANO + f"{a} - {nome.capitalize()} | Nota: {nota}" + RESET)
            time.sleep(0.3)
    print()


# ===== INÍCIO =====
carregar()

print(AZUL + NEGRITO + "=== SISTEMA DE GESTÃO DE ALUNOS V2.0 ===" + RESET)
print()
print(AMARELO + "Dados salvos automaticamente em alunos.json" + RESET)
print()

while True:
    menu()

    try:
        resposta = int(input("Digite aqui: "))
    except ValueError:
        print(VERMELHO + "Digite apenas números." + RESET)
        continue

    # VER ALUNOS
    if resposta == 1:
        turma()

    # ALTERAR NOTA
    elif resposta == 2:
        turma()
        r1 = input("Digite o nome do aluno: ").lower()

        try:
            r2 = float(input("Digite a nova nota (0 a 10): "))
        except ValueError:
            print(VERMELHO + "Nota inválida." + RESET)
            continue

        if 0 <= r2 <= 10:
            for aluno in alunos:
                if r1 in aluno:
                    aluno[r1] = r2
                    salvar()
                    print(VERDE + "Nota alterada com sucesso!" + RESET)
                    break
            else:
                print(VERMELHO + "Aluno não encontrado." + RESET)
        else:
            print(VERMELHO + "A nota deve estar entre 0 e 10." + RESET)

    # REMOVER
    elif resposta == 3:
        turma()
        try:
            r3 = int(input("Digite o número do aluno que deseja remover: "))
        except ValueError:
            print(VERMELHO + "Digite um número válido." + RESET)
            continue

        if 1 <= r3 <= len(alunos):
            alunos.pop(r3 - 1)
            salvar()
            print(VERDE + "Aluno removido com sucesso!" + RESET)
        else:
            print(VERMELHO + "Número inválido." + RESET)

    # ADICIONAR
    elif resposta == 4:
        print()
        print(AZUL + NEGRITO + "=== MODO ADIÇÃO CONTÍNUA ===" + RESET)
        print(AMARELO + "Digite 'parar' para voltar ao menu." + RESET)
        print()

        while True:
            aluno = input("Digite o nome do aluno: ").lower()

            if aluno == "parar":
                break

            dic = {aluno: random.randint(0, 10)}
            alunos.append(dic)
            salvar()
            print(VERDE + "Aluno adicionado com sucesso!" + RESET)

    # FECHAR
    elif resposta == 0:
        print(VERMELHO + "Fechando programa..." + RESET)
        time.sleep(2)
        print(VERDE + "Programa fechado com sucesso!" + RESET)
        break

    else:
        print(VERMELHO + "Opção inválida." + RESET)