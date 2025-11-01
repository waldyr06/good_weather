import time

# VARIÁVEL GLOBAL: Usamos uma lista para que a função possa modificar o valor
TIMER_ID = [None] 

def foco(segundos_totais_foco, label_min, label_seg, root): 
    def atualizar():
        nonlocal segundos_totais_foco 
        # Apenas se o tempo não acabou
        if segundos_totais_foco >= 0:           
            minutos, segundos = divmod(segundos_totais_foco, 60)
            label_min.config(text=f"{minutos:02}")
            label_seg.config(text=f"{segundos:02}")
        
            segundos_totais_foco -= 1            
            

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
        

def pausa_leve(segundos_totais_pausa_leve, label_min2, label_seg2, root): 
    def atualizar():
        nonlocal segundos_totais_pausa_leve
        # Apenas se o tempo não acabou
        if segundos_totais_pausa_leve >= 0:           
            minutos, segundos = divmod(segundos_totais_pausa_leve, 60)
            label_min2.config(text=f"{minutos:02}")
            label_seg2.config(text=f"{segundos:02}")
        
            segundos_totais_pausa_leve -= 1            
            

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
        

def pausa_longa(segundos_totais_pausa_longa, label_min3, label_seg3, root): 
    def atualizar():
        nonlocal segundos_totais_pausa_longa
        # Apenas se o tempo não acabou
        if segundos_totais_pausa_longa >= 0:           
            minutos, segundos = divmod(segundos_totais_pausa_longa, 60)
            label_min3.config(text=f"{minutos:02}")
            label_seg3.config(text=f"{segundos:02}")
        
            segundos_totais_pausa_longa -= 1            
            

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

def reiniciar(funcao): #reinicia uma das contagens
    if funcao == foco:
        foco(1500)
    if funcao == pausa_leve:
        pausa_leve(300)
    if funcao == pausa_longa:
        pausa_longa(900)