from modelos import Conta_Bancária
import sys # Fecha o programa
import smtplib # permite ao Python enviar e-mails usando o protocolo SMTP (Simple Mail Transfer Protocol).
import random
from email.mime.text import MIMEText # Ela é usada para criar o conteúdo do e-mail de forma organizada.

nova_conta = None

while True:
    print("=== BANCO PYTHON ===\n")

    opcoes = int(input("Escolha uma opção:\n 1 - Criar conta\n 2 - Depositar\n 3 - Sacar\n 4 - Sair\n"))

    if opcoes == 1:
        nome = str(input("Qual o seu nome?\n"))
        idade = int(input("Qual a sua idade?\n"))
        endereco = str(input("Qual o seu endereço?\n"))
        telefone = int(input("Qual o número do seu telefone?\n"))
        email = str(input("Qual o seu e-mail?\n"))

        # O python vai gerar um código aleatório
        codigo = random.randint(100000, 999999)

        email_remetente = "SEU_EMAIL@gmail.com" # O email de quem manda
        senha_app = "SUASENHADEAPP" # A senha do email do remetente

        email_destino = email # O email de quem vai receber o email do remetente

        mensagem = MIMEText(f"Olá {nome}, este é o seu código: {codigo}") # A mensagem que será mandada
        mensagem["Subject"] = "Código de verificação" # Define o assunto do email
        mensagem["From"] = email_remetente # Diz quem manda
        mensagem["To"] = email_destino #Diz quem recebe

        #enviar email
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
                servidor.login(email_remetente, senha_app)
                servidor.send_message(mensagem)

            print("Um código foi enviado ao seu email")

        except Exception as e:
            print("Como o envio falhou, por favor tente novamente")
            sys.exit() # Fecha todo o programa

        codigo_certo = int(input("Digite o código enviado ao seu email: \n"))
        if codigo_certo == codigo:
            numero_conta = random.randint(100000, 999999)

            nova_conta = Conta_Bancária(nome, numero_conta, idade, endereco, telefone, email, 0.0)

            print(f"{nome}, sua conta foi criada com sucesso!")
            print(f"Seu número da conta é {numero_conta}")

        else:
            print("Código incorreto!")
            sys.exit() # Fecha todo o programa

    elif opcoes == 2:
        if nova_conta is None:
            print("\nVocê precisa criar uma conta antes de depositar!\n")

        deposito = float(input("Qual o valor do deposito?\n"))
        nova_conta.depositar(deposito)

    elif opcoes == 3:
        if nova_conta is None:
            print("\nVocê precisa criar uma conta antes de depositar!\n")
            
        saque = float(input("Qual o valor do saque?\n"))
        nova_conta.sacar((saque))
    
    elif opcoes == 4:
        sys.exit() # Fecha todo o programa

    else:
        print("Escolha uma das 4 opções")
        continue
