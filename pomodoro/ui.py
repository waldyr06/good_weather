import tkinter as tk
import timer

#Espaço para eu armazenar o tempo de cada uma das variaveis em segundos
segundos_totais = 1500

root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("1366x768")
root.configure(bg="#f0f0f0")

# Frame principal (parte superior)
top_frame = tk.Frame(root)
top_frame.pack(fill="both", expand=True)

# Blocos principais
frame_foco = tk.Frame(top_frame, bg="#FFF2F2")
frame_pausa_leve = tk.Frame(top_frame, bg="#F2FFF5")
frame_pausa_longa = tk.Frame(top_frame, bg="#F2F9FF")

frame_foco.pack(side="left", fill="both", expand=True)
frame_pausa_leve.pack(side="left", fill="both", expand=True)
frame_pausa_longa.pack(side="left", fill="both", expand=True)

# --- BLOCO FOCO ---
titulo = tk.Label(frame_foco, text="Foco", bg=frame_foco["bg"], fg="#471515", font=("Arial", 16, "bold"))
titulo.place(relx=0.5, rely=0.15, anchor="center")

foco_container = tk.Frame(frame_foco, bg=frame_foco["bg"])
foco_container.pack(expand=True)

label_min = tk.Label(foco_container, text="00", bg=frame_foco["bg"], fg="#471515", font=("Arial", 130, "bold"), anchor="center")
label_min.pack(expand=True)

label_seg = tk.Label(foco_container, text="00", bg=frame_foco["bg"], fg="#471515", font=("Arial", 130, "bold"), anchor="center")
label_seg.pack() 

botao_foco = tk.Button(foco_container, command=lambda: timer.foco(segundos_totais, label_min, label_seg, root), text=">", bg=frame_foco["bg"], fg="#471515", font=("Arial", 20, "bold"), border=10, relief=tk.FLAT)
botao_foco.pack(side='bottom')

# --- BLOCO PAUSA LEVE ---
titulo1 = tk.Label(frame_pausa_leve, text="Pausa Leve", bg=frame_pausa_leve["bg"], fg="#14401D", font=("Arial", 16, "bold"))
titulo1.place(relx=0.5, rely=0.15, anchor="center")

pausa_leve_container = tk.Frame(frame_pausa_leve, bg=frame_pausa_leve["bg"])
pausa_leve_container.pack(expand=True)

botao_pausa_leve = tk.Button(pausa_leve_container, text=">", bg=frame_pausa_leve["bg"], fg="#14401D", font=("Arial", 20, "bold"), border=10, relief=tk.FLAT)
botao_pausa_leve.pack(side='bottom')

tk.Label(pausa_leve_container, text="00", bg=frame_pausa_leve["bg"], fg="#14401D",
         font=("Arial", 130, "bold"), anchor="center").pack(expand=True)
tk.Label(pausa_leve_container, text="00", bg=frame_pausa_leve["bg"], fg="#14401D",
         font=("Arial", 130, "bold"), anchor="center").pack()

# --- BLOCO PAUSA LONGA ---
titulo2 = tk.Label(frame_pausa_longa, text="Pausa Longa", bg=frame_pausa_longa["bg"], fg="#153047", font=("Arial", 16, "bold"))
titulo2.place(relx=0.5, rely=0.15, anchor="center")

pausa_longa_container = tk.Frame(frame_pausa_longa, bg=frame_pausa_longa["bg"])
pausa_longa_container.pack(expand=True)

botao_pausa_longa = tk.Button(pausa_longa_container, text=">", bg=frame_pausa_longa["bg"], fg="#153047", font=("Arial", 20, "bold"), border=10, relief=tk.FLAT)
botao_pausa_longa.pack(side='bottom')

tk.Label(pausa_longa_container, text="00", bg=frame_pausa_longa["bg"], fg="#153047",
         font=("Arial", 130, "bold"), anchor="center").pack(expand=True)
tk.Label(pausa_longa_container, text="00", bg=frame_pausa_longa["bg"], fg="#153047",
         font=("Arial", 130, "bold"), anchor="center").pack()

root.mainloop()