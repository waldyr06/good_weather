import tkinter as tk

root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("1366x768")
root.configure(bg="#f0f0f0")

# Frame principal (parte superior)
top_frame = tk.Frame(root)
top_frame.pack(fill="both", expand=True)

# Blocos principais
frame_foco = tk.Frame(top_frame, bg="#FFE0E0")
frame_pausa_leve = tk.Frame(top_frame, bg="#DFFFDF")
frame_pausa_longa = tk.Frame(top_frame, bg="#DCE6FF")

frame_foco.pack(side="left", fill="both", expand=True)
frame_pausa_leve.pack(side="left", fill="both", expand=True)
frame_pausa_longa.pack(side="left", fill="both", expand=True)

# --- BLOCO FOCO ---
titulo = tk.Label(frame_foco, text="Foco", bg=frame_foco["bg"], fg="black", font=("Arial", 16, "bold"))
titulo.place(relx=0.5, rely=0.15, anchor="center")

foco_container = tk.Frame(frame_foco, bg=frame_foco["bg"])
foco_container.pack(expand=True)

tk.Label(foco_container, text="00", bg=frame_foco["bg"], fg="black",
         font=("Arial", 150, "bold"), anchor="center").pack(expand=True)
tk.Label(foco_container, text="00", bg=frame_foco["bg"], fg="black",
         font=("Arial", 150, "bold"), anchor="center").pack()

# --- BLOCO PAUSA LEVE ---
titulo1 = tk.Label(frame_pausa_leve, text="Pausa Leve", bg=frame_pausa_leve["bg"], fg="black", font=("Arial", 16, "bold"))
titulo1.place(relx=0.5, rely=0.15, anchor="center")

pausa_leve_container = tk.Frame(frame_pausa_leve, bg=frame_pausa_leve["bg"])
pausa_leve_container.pack(expand=True)

tk.Label(pausa_leve_container, text="00", bg=frame_pausa_leve["bg"], fg="black",
         font=("Arial", 150, "bold"), anchor="center").pack(expand=True)
tk.Label(pausa_leve_container, text="00", bg=frame_pausa_leve["bg"], fg="black",
         font=("Arial", 150, "bold"), anchor="center").pack()

# --- BLOCO PAUSA LONGA ---
titulo2 = tk.Label(frame_pausa_longa, text="Pausa Longa", bg=frame_pausa_longa["bg"], fg="black", font=("Arial", 16, "bold"))
titulo2.place(relx=0.5, rely=0.15, anchor="center")

pausa_longa_container = tk.Frame(frame_pausa_longa, bg=frame_pausa_longa["bg"])
pausa_longa_container.pack(expand=True)

tk.Label(pausa_longa_container, text="00", bg=frame_pausa_longa["bg"], fg="black",
         font=("Arial", 150, "bold"), anchor="center").pack(expand=True)
tk.Label(pausa_longa_container, text="00", bg=frame_pausa_longa["bg"], fg="black",
         font=("Arial", 150, "bold"), anchor="center").pack()

root.mainloop()