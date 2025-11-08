from pomodoro import settings
from pomodoro.sounds import sons

# VARIÁVEL GLOBAL: Uma lista para que a função possa modificar o valor
TIMER_ID = [None] 

def foco(segundos_totais_foco=None, label_min=None, label_seg=None, root=None):
    if segundos_totais_foco is None:
        segundos_totais_foco = settings.tempo_foco
    def atualizar():
        nonlocal segundos_totais_foco 
        if segundos_totais_foco >= 0:           
            minutos, segundos = divmod(segundos_totais_foco, 60)
            label_min.config(text=f"{minutos:02}")
            label_seg.config(text=f"{segundos:02}")
        
            segundos_totais_foco -= 1            
            
            TIMER_ID[0] = root.after(1000, atualizar) 
            
        
        # Limpar o ID do timer quando terminar
        else:
            sons.tocar_som()
            TIMER_ID[0] = None 


    # Cancela qualquer timer anterior se o botão for pressionado enquanto um timer roda
    if TIMER_ID[0]:
        root.after_cancel(TIMER_ID[0])
        TIMER_ID[0] = None # Limpa o ID      
    # Inicia a contagem
    atualizar()        
        
def pausa_leve(segundos_totais_pausa_leve=None, label_min2=None, label_seg2=None, root=None):
    if segundos_totais_pausa_leve is None:
        segundos_totais_pausa_leve = settings.tempo_pausa_leve
    def atualizar():
        nonlocal segundos_totais_pausa_leve
        if segundos_totais_pausa_leve >= 0:           
            minutos, segundos = divmod(segundos_totais_pausa_leve, 60)
            label_min2.config(text=f"{minutos:02}")
            label_seg2.config(text=f"{segundos:02}")
        
            segundos_totais_pausa_leve -= 1            
            

            TIMER_ID[0] = root.after(1000, atualizar) 
            
        
        # Limpar o ID do timer quando terminar
        else:
            sons.tocar_som()
            TIMER_ID[0] = None 

    # Cancela qualquer timer anterior se o botão for pressionado enquanto um timer roda
    if TIMER_ID[0]:
        root.after_cancel(TIMER_ID[0])
        TIMER_ID[0] = None # Limpa o ID      
    # Inicia a contagem
    atualizar()          
        
def pausa_longa(segundos_totais_pausa_longa=None, label_min3=None, label_seg3=None, root=None):
    if segundos_totais_pausa_longa is None:
        segundos_totais_pausa_longa = settings.tempo_pausa_longa 
    def atualizar():
        nonlocal segundos_totais_pausa_longa
        if segundos_totais_pausa_longa >= 0:           
            minutos, segundos = divmod(segundos_totais_pausa_longa, 60)
            label_min3.config(text=f"{minutos:02}")
            label_seg3.config(text=f"{segundos:02}")
        
            segundos_totais_pausa_longa -= 1            
            

            TIMER_ID[0] = root.after(1000, atualizar) 
            
        # Limpar o ID do timer quando terminar
        else:
            sons.tocar_som
            TIMER_ID[0] = None 
 
    # Cancela qualquer timer anterior se o botão for pressionado enquanto um timer roda
    if TIMER_ID[0]:
        root.after_cancel(TIMER_ID[0])
        TIMER_ID[0] = None # Limpa o ID      
    # Inicia a contagem
    atualizar()