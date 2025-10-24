import time

def foco(segundos_totais): #1500 segundos para chegar nos 25 minutos
        pausa = False
        while segundos_totais > 0:
            try:    
                if not pausa:
                    minutos, segundos = divmod(segundos_totais, 60)
                    print(f"{minutos:02} : {segundos:02}")
                    time.sleep(1)
                    segundos_totais -= 1
                else:
                    time.sleep(1)

            except  KeyboardInterrupt:
                pausa = not pausa
                #if pausa: 
                    #print("Pausado!")
                #else:
                    #print("Voltando")
        #print("Ciclo de foco concluído!")         
        

def pausa_leve(segundos_totais): #300 segundos para chegar nos 5 minutos
        pausa = False
        while segundos_totais > 0:
            try:
                if not pausa:
                    minutos, segundos = divmod(segundos_totais, 60)
                    print(f"{minutos:02} : {segundos:02}")
                    time.sleep(1)
                    segundos_totais -= 1
                else:
                    time.sleep(1)

            except  KeyboardInterrupt:
                 pausa = not pausa
                 #if pausa:
                     #print("Pausando")
                 #else:
                    #print("Voltando")
        #print("Ciclo de pausa leve concluído!")     
        

def pausa_longa(segundos_totais): #900 segundos para chegar nos 15 minutos#
        pausa = False
        while segundos_totais > 0:
            try:
                if not pausa:
                    minutos, segundos = divmod(segundos_totais, 60)
                    print(f"{minutos:02} : {segundos:02}")
                    time.sleep(1)
                    segundos_totais -= 1
                else:
                    time.sleep(1)

            except  KeyboardInterrupt:
                pausa = not pausa
                #if pausa:
                    #print("Pausando")
                #else:
                    #print("Voltando")
        #print ("Ciclo de pausa longa concluído!")

def reiniciar(funcao): #reinicia uma das contagens
    if funcao == foco:
        foco(1500)
    if funcao == pausa_leve:
        pausa_leve(300)
    if funcao == pausa_longa:
        pausa_longa(900)