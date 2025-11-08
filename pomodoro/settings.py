# Valores padrão (em segundos)
TEMPO_FOCO_PADRAO = 25 * 60    # 25 minutos
TEMPO_PAUSA_LEVE_PADRAO = 5 * 60 # 5 minutos
TEMPO_PAUSA_LONGA_PADRAO = 15 * 60 # 15 minutos

# Variáveis ativas — começam com os valores padrão
tempo_foco = TEMPO_FOCO_PADRAO
tempo_pausa_leve = TEMPO_PAUSA_LEVE_PADRAO
tempo_pausa_longa = TEMPO_PAUSA_LONGA_PADRAO


def atualizar_tempos(novo_foco=None, nova_pausa_leve=None, nova_pausa_longa=None):
    """
    Atualiza os tempos globais de foco e pausas.
    Só muda o que for passado (os outros permanecem iguais).
    """
    global tempo_foco, tempo_pausa_leve, tempo_pausa_longa

    if novo_foco is not None:
        tempo_foco = novo_foco * 60  # converte minutos pra segundos

    if nova_pausa_leve is not None:
        tempo_pausa_leve = nova_pausa_leve * 60

    if nova_pausa_longa is not None:
        tempo_pausa_longa = nova_pausa_longa * 60