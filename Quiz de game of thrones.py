import os 

perguntas_respostas = [
        {
            'Pergunta': "Quem são os irmãos do rei Joffrey?",
            'Opções': ['Tommen e Myrcella', 'Hodor e rickon', 'tyrion e Myrcella', 'JTywin e tommen','Hodor e jaime'],
            'Resposta': 'Tommen e Myrcella',
        },
        {
            'Pergunta': 'Quem é o senhor das ilhas de Ferro?',
            'Opções': ['Ned Stark', 'Balon Greyjoy', 'Jon Snow', 'Jorah Mormont', 'Khal Drogo'],
            'Resposta': 'Balon Greyjoy',
        },
        {
            'Pergunta': 'Qual é o nome do(a) protagonista da primeira temporada de Game of Thrones?',
            'Opções': ['Tyrion Lannister', 'Eddard Stark', 'Jaime Lannister', 'Catelyn Stark', 'Robert Baratheon'],
            'Resposta': 'Eddard Stark',
        },
        {
            'Pergunta': 'Qual é o nome da espada usada por Arya Stark?',
            'Opções': ['Gelo', 'Garra Longa', 'Agulha', 'Noite Sombria', 'Garra de Lobo'],
            'Resposta': 'Agulha',
        },
        {
            'Pergunta': 'Quem é a selvagem que Jon Snow ama?',
            'Opções': ['Catelyn', 'Meera', 'Ygritte', 'Elysa', 'Jorah'],
            'Resposta': 'Ygritte',
        },
    ]
    
def funcionamento_das_perguntas(perguntas):
    qtd_acertos = 0
    for pergunta in perguntas:
        print(pergunta['Pergunta'])
        print()

        opcoes = pergunta['Opções']
        for numero, opcao in enumerate(opcoes, start=1):
            print(f'{numero}) {opcao}')
            print()

        print("Aperte 0 para voltar ao menu")
        escolha = input('Escolha uma opção: ')

        acertou = False
        escolha_int = None
        qtd_opcoes = len(opcoes)

        if escolha.isdigit():
            escolha_int = int(escolha)

        if escolha_int == 0:
            os.system('cls')
            opcao_menu()

        if escolha_int is not None:
            if 1 <= escolha_int <= qtd_opcoes:
                if opcoes[escolha_int - 1] == pergunta['Resposta']:
                    acertou = True

        print()
        if acertou:
            os.system('cls')
            qtd_acertos += 1
            print("Acertou 👍")
            print(' ')
        else:
            os.system('cls')
            print("Errou ❌")
            print(' ')

    
    print(f'Você acertou {qtd_acertos}')
    print(f'de {len(perguntas)} perguntas.')

    qualquer = input("Precione qualquer tecla para voltar ao menu: ")
    os.system('cls')



def nova_pergunta_e_respostas():
    nova_pergunta = input("NOVA PERGUNTA: ")
    opcoes = input("OPÇÕES (separadas por vírgula): ").split(',')
    nova_resposta = input("NOVA RESPOSTA: ")
    
    nova_entrada = {
        'Pergunta': nova_pergunta,
        'Opções': [opcao.strip() for opcao in opcoes],
        'Resposta': nova_resposta
    }
    
    perguntas_respostas.append(nova_entrada)


def buscar_resposta(perguntas_respostas):
    buscando_pergunta = input("Digite a pergunta: ")
    for pergunta in perguntas_respostas:
        if pergunta['Pergunta'].lower() == buscando_pergunta.lower():
            print(f"Resposta: {pergunta['Resposta']}")
            return
    print("Pergunta não encontrada.")
    print("Aperte [0] para voltar ao menu ou [1] para tentar novamente:")
    
    tentar = int(input("Escolha uma opção: "))

    if tentar == 0:
        os.system('cls')
        opcao_menu()
        
    elif tentar == 1:
        os.system('cls')
        buscar_resposta(perguntas_respostas)
        
    else:
        print("somente 0 ou 1.")
        os.system('cls')



def exibir_perguntas_e_respostas():
    for letra in perguntas_respostas:
        print(f"Pergunta: {letra['Pergunta']}")
        print(f"Resposta: {letra['Resposta']}")
        print()



def exibir_menu():
    print("[1] Perguntas e Respostas:")
    print("[2] Adicionar uma nova pergunta")
    print("[3] Exibir todas as perguntas e respostas")
    print("[4] Buscar uma resposta com base em uma pergunta")

def opcao_menu():
    exibir_menu()
    menu = int(input("Escolha uma opção: "))
    os.system('cls')

    
    if menu == 1:
        funcionamento_das_perguntas(perguntas_respostas)

    elif menu == 2:
        nova_pergunta_e_respostas()

    elif menu == 3:
        exibir_perguntas_e_respostas()
        escolha = int(input('Aperte para 0 voltar ao menu: '))

        if escolha == 0:
            os.system('cls')
            opcao_menu()
    
    elif menu == 4:
        buscar_resposta(perguntas_respostas)



def menu_principal():
        while True:
            print('Perguntas e Respostas: ⚔️ 🤴')
            print(f' '*5,'GAME OF THRONES ')
            qualquer = input("Precione qualquer tecla para começar: ")
            os.system('cls')
            opcao_menu()




menu_principal()