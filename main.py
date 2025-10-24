from pomodoro import timer

while True:
    opcao = input("Digite qual modo você quer: 1 - Foco. 2 - Pausa leve. 3 - Pausa longa. 4 - SAIR: ")
    match opcao:
        case "1":
            #print("Foco Ativado")
            timer.foco(1500)
    
        case "2":
            #print("Pausa leve ativada")
            timer.pausa_leve(300)

        case "3":
            #print("Pausa longa ativada")
            timer.pausa_longa(900)

        case "4":
            break

        case _:
            "Você digitou uma opçãop inexistente"
#print("FECHOU!!!")