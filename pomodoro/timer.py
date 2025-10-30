import time

# VARIÁVEL GLOBAL: Usamos uma lista para que a função possa modificar o valor
TIMER_ID = [None] 

def foco(segundos_totais, label_min, label_seg, root): 
    def atualizar():
        nonlocal segundos_totais 
        # Apenas se o tempo não acabou
        if segundos_totais >= 0:           
            minutos, segundos = divmod(segundos_totais, 60)
            label_min.config(text=f"{minutos:02}")
            label_seg.config(text=f"{segundos:02}")
        
            segundos_totais -= 1            
            

            TIMER_ID[0] = root.after(1000, atualizar) 
            
        else:
             #provavel que vai da erro, não pode ter print
             print("Fim do Tempo de Foco!")
             # Limpar o ID do timer quando terminar
             TIMER_ID[0] = None 


    # 2. LÓGICA DE INÍCIO DA FUNÇÃO FOCO (Chamada pelo botão)    
    # Cancela qualquer timer anterior se o botão for pressionado enquanto um timer roda
    if TIMER_ID[0]:
        root.after_cancel(TIMER_ID[0])
        TIMER_ID[0] = None # Limpa o ID      
    # Inicia a contagem
    atualizar()        
        

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