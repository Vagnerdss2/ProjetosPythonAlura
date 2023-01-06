import random

def jogar():

    print('*'*60)
    print('JOGO DE ADIVINHAÇÃO'.center(60))


    numero_aleatorio = random.randint(1,51)
    numero_tentativas = 0
    tentativas_realizadas = 1
    chutes = 0
    pontos = 1000

    print('Nível de dificuldade: (1) Facil  (2) Médio (3) Difícil.')
    nivel_dificuldade = int(input('Escolha seu nivel de dificuldade: ')) 

    if nivel_dificuldade == 1:
        numero_tentativas = 20
    elif nivel_dificuldade == 2:
        numero_tentativas = 10
    elif nivel_dificuldade == 3:
        numero_tentativas = 5

    for rodadas in range( 1,numero_tentativas + 1):
        chutes += 1
        
        print('*'*60)
        print('numero de tentativas: '.upper(),tentativas_realizadas,' de ',numero_tentativas)
        entrada = int(input('Chute um numero de 1 a 50: ',))
        
        if numero_tentativas == chutes:
            print('Seus chutes se esgotaram, VOCÊ PERDEU!!!')
            print('O numero secreto era: ',numero_aleatorio)
            break
        if entrada < 1 or entrada > 50:
            print('Você precisa digitar um numero entre 1 e 50!')
            continue

        acertou = numero_aleatorio == entrada
        numero_maior = entrada > numero_aleatorio
        numero_menor = entrada < numero_aleatorio

        if acertou:
            print('Parabéns, você acertou!!!')
            print('Numero secreto: ', numero_aleatorio)
            print('Seu chute: ', entrada)
            print(f'Você fez um total de {pontos} pontos')
            break
        else:
            if numero_maior:
                print('Seu chute foi acima, tente novamente!')
            elif numero_menor:
                print('Seu chute foi abaixo, tente novamente!')
            pontos_perdidos = abs(chutes - numero_aleatorio) # o abs foi usado para o calculo não ficar negativo, trazendo assim só os numeros positivos
            pontos = pontos -  pontos_perdidos   
        
        tentativas_realizadas += 1

if(__name__ == '__main__'):
    jogar()




    