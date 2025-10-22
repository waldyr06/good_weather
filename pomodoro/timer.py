import time

print("teste de lógica do tempo pomodoro em python")

def foco(segundos_totais): #1500 segundos para chegar nos 25 minutos
    try:
        pausa = False
        while segundos_totais > 0:
            if not pausa:
                minutos, segundos = divmod(segundos_totais, 60)
                print(f"{minutos:02} : {segundos:02}")
                time.sleep(1)
                segundos_totais -= 1  
        print("ACABOU O FOCO") 
    except  KeyboardInterrupt:
        print("Você pausou o tempo!!!")
    print("ACABOU!!!")

def pausa_leve(segundos_totais): #300 segundos para chegar nos 5 minutos
    try:
        pausa = False
        while segundos_totais > 0:
            if not pausa:
                minutos, segundos = divmod(segundos_totais, 60)
                print(f"{minutos:02} : {segundos:02}")
                time.sleep(1)
                segundos_totais -= 1
        print("ACABOA PAUSA LEVE")
    except  KeyboardInterrupt:
        print("Você pausou o tempo!!!")
    print("ACABOU!!!")

def pausa_longa(segundos_totais): #900 segundos para chegar nos 15 minutos
    try:
        pausa = False
        while segundos_totais > 0:
            if not pausa:
                minutos, segundos = divmod(segundos_totais, 60)
                print(f"{minutos:02} : {segundos:02}")
                time.sleep(1)
                segundos_totais -= 1
        print("ACABOU A PAUSA LONGA")
    except  KeyboardInterrupt:
        print("Você pausou o tempo!!!")
    print("ACABOU!!!")

def reiniciar(funcao): #reinicia uma das contagens
    if funcao == foco:
        foco(1500)
    if funcao == pausa_leve:
        pausa_leve(300)
    if funcao == pausa_longa:
        pausa_longa(900)