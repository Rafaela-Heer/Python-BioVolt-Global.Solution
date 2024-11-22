import os
from pathlib import Path

caminho_arquivo = Path.home() / "Desktop" / "candidatos.txt"

# Função para coletar e validar as informações dos candidatos
def obter_candidato():
    
    nome = input('Digite o nome do candidato: ')
    
    # Loop de validação do CPF: deve conter 11 dígitos numéricos
    while True:
        cpf = input('Digite o seu CPF (apenas números): ')
        if cpf.isnumeric() and len(cpf) == 11:
            cpf = int(cpf)
            break
        print('Digite o seu CPF Correto.')
    
    # Loop de validação da idade: deve ser numérica e maior que 18
    while True:
        idade = input('Digite a sua idade: ')
        if idade.isnumeric() and int(idade):
            idade = int(idade)
            if idade >= 18:
                break
            else:
                print('Você deve ser maior de idade para se candidatar a essa vaga!')
                return
        else:
            print('Por favor digite apenas números válidos.')

    email_contato = input('Digite o seu email para contato: ')
    
    # Loop de validação da experiência: deve ser um valor numérico
    while True:
        experiencia = input('Quantos anos você tem de experiência (Tempo em números)? ')
        if experiencia.isnumeric():
            experiencia = int(experiencia)
            break
        else:
            print('Digite apenas números!')
    
    competencias = input('Quais as suas competências para a vaga? ')

    # Estrutura dos dados do candidato em formato de dicionário
    return {
        'nome': nome,
        'idade': idade,
        'experiencia': experiencia,
        'cpf': cpf,
        'email': email_contato,
        'qualificacoes': competencias
    }
    
# Salva os candidatos dentro de um arquivo txt.
def salvar_candidato(candidato):
    
    with open(caminho_arquivo, 'a') as arquivo:
        candidato_info = f"\nNome: {candidato['nome']}\nCPF: {candidato['cpf']}\nIdade: {candidato['idade']}\nEmail: {candidato['email']}\nExperiencia: {candidato['experiencia']} anos\nCompetencias: {candidato['qualificacoes']}\n"
        arquivo.write(candidato_info)

# Função para ler e processar o arquivo txt com a lista de candidatos
def ler_candidatos():
    
    candidatos = []
    with open(caminho_arquivo, 'r') as arquivo:
        conteudo = arquivo.read().strip()
    
    # Divide o conteúdo por candidato (separados por linha em branco)
    if conteudo:
        candidatos_info = conteudo.split("\n\n")
        for candidato_info in candidatos_info:
            
            # Divide as informações de cada candidato em linhas
            dados = candidato_info.split("\n")
            
            # Processa cada linha e cria um dicionário com os dados
            candidato = {}
            for linha in dados:
                identificar, valor = linha.split(": ", 1)
                candidato[identificar.lower()] = valor

            candidatos.append(candidato)
    
    return candidatos

# Função para exibir todos os candidatos cadastrados
def mostrar_candidatos(): 
    
    candidatos = ler_candidatos()
    if candidatos:
        print("\nCandidatos Cadastrados")
        for candidato in candidatos:
            print(f"\nNome: {candidato['nome']}")
            print(f"Idade: {candidato['idade']}")
            print(f"Experiencia: {candidato['experiencia']} anos")
            print(f"CPF: {candidato['cpf']}")
            print(f"Email: {candidato['email']}")
            print(f"Competencias: {candidato['competencias']}")
    else:
        print("\nNenhum candidato registrado.")

# Função que controla o fluxo do programa
def main():
    
    # Menu de cadastro
    while True:
        print("\nSistema de Cadastro\n")
        print("1. Cadastrar Candidato")
        print("2. Ver Candidatos")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        # Só salva se o candidato for válido
        if opcao == "1":
            candidato = obter_candidato()
            if candidato:
                salvar_candidato(candidato)
                print("\nCadastro realizado com sucesso!")
                
        # Mostra a lista de candidatos salvos
        elif opcao == "2": 
            mostrar_candidatos()
            
        # Encerra o sistema
        elif opcao == "3": 
            print("\nEncerrando o sistema.")
            break
        
        else:
            print("\nOpção inválida!")

# Ponto de start do programa.
main()
