import socket

# Guardar a questão desejada (Retorna um inteiro)
def get_question():
    while True:
        question = int(input('Digite a questão a ser realizada: '))
        if question >= 1 and question <= 7:
            return question
        print(f'{question} não é uma questão valida.\nTente novamente.\n')


# Salvar os parâmetros das questões especificadas pelo cliente (Retornam Strings)
# Questão 1 

def get_question1_parameters():
    value = input('Digite o valor a ser convertido: ')
    from_base = input('Digite a base de origem (bin/dec/hex): ')
    to_base = input('Digite a base de destino (bin/dec/hex): ')
    return f"{value},{from_base},{to_base}"

def get_question2_parameters():
    value1 = input('Digite o primeiro valor a ser operado: ')
    value2 = input('Digite o segundo valor a ser operado: ')
    operator = input('Digite a operação a ser realizada ( + | - | * | / ): ')
    return f"{value1},{value2},{operator}"

# Questão 4
def get_question4_parameters():
    number = input('Digite o valor decimal qualquer: ')
    return number

# Questão 5
def get_question5_parameters():
    texto = input('Digite o texto a ser codificado: ')
    return texto

# Questão 6
def get_question6_parameters():
    expressao = input('Digite a expressão que deverá ser desenhada: ')
    return expressao

# Questão 7
def get_question7_parameters():
    while True:
        print('Digite se as variaveis a seguir são True ou False: \n')
        A = input('A: ')
        B = input('B: ')
        C = input('C: ')
        if (A != 'True' and A != 'False') or (B != 'True' and B != 'False') or (C != 'True' and C != 'False'):
            print('Tente novamente: \n')
        else:
            break
    return f"{A},{B},{C}"

def start_client(host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        question = get_question()
        print(f'Você selecionou a questão {question}.\n')
        s.sendall(str(question).encode()) # Primeiro envia a questão para o servidor Str --> bytes

        if question == 1:
            params = get_question1_parameters()
        elif question == 2:
            params = get_question2_parameters()
        elif question == 4:
            params = get_question4_parameters()
        elif question == 5:
            params = get_question5_parameters()
        elif question == 6:
            params = get_question6_parameters()
        elif question == 7:
            params = get_question7_parameters()

        
        s.sendall(params.encode()) # Envia os parametros em bytes. (String --> bytes)


        # Se a questão selecionada for a 6, o cliente receberá apenas o arquivo.
        if question == 6:
            with open('circuito.jpg', 'wb') as file:
                while True:
                    dados = s.recv(10000)
                    if not dados:
                        break
                    file.write(dados)

            print('Desenho recebido com sucesso')

        else:
            result = s.recv(1024) # Recebe os dados do servidor em bytes e decodifica para string 
            print(f'Resposta do servidor:\n{result.decode()}')

if __name__ == "__main__":
    start_client()
